// Copyright 2022 The Matrix.org Foundation C.I.C.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#![forbid(unsafe_code)]
#![deny(clippy::all)]
#![warn(clippy::pedantic)]
#![allow(clippy::needless_pass_by_value)]

use std::time::Duration;

use anyhow::{anyhow, Context};
use bytesize::ByteSize;
use http_body::Body;
use matrix_http_rendezvous::{DEFAULT_MAX_BYTES, DEFAULT_MAX_ENTRIES, DEFAULT_TTL};
use pyo3::prelude::*;
use pyo3_matrix_synapse_module::{parse_config, ModuleApi};
use serde::Deserialize;
use tower::ServiceExt;

const fn default_ttl() -> Duration {
    DEFAULT_TTL
}

const fn default_max_bytes() -> ByteSize {
    ByteSize(DEFAULT_MAX_BYTES as u64)
}

const fn default_max_entries() -> usize {
    DEFAULT_MAX_ENTRIES
}

#[pyclass]
#[derive(Deserialize)]
struct Config {
    prefix: String,

    #[serde(default = "default_ttl", with = "humantime_serde")]
    ttl: Duration,

    #[serde(default = "default_max_bytes")]
    max_bytes: ByteSize,

    #[serde(default = "default_max_entries")]
    max_entries: usize,
}

#[pyclass]
pub struct SynapseRendezvousModule;

#[pymethods]
impl SynapseRendezvousModule {
    #[new]
    fn new(config: &Config, module_api: ModuleApi) -> PyResult<Self> {
        tracing::info!(
            "Mounting rendez-vous server on {prefix}, with a TTL of {ttl} and max payload size of {max_bytes}",
            prefix = config.prefix,
            ttl = humantime::format_duration(config.ttl),
            max_bytes = config.max_bytes.to_string_as(true),
        );

        let max_bytes = config
            .max_bytes
            .0
            .try_into()
            .context("Could not convert max_bytes from config")?;

        let sessions = matrix_http_rendezvous::Sessions::new(config.ttl, config.max_entries);
        pyo3_asyncio::tokio::get_runtime().spawn(sessions.eviction_task(Duration::from_secs(60)));

        let service = matrix_http_rendezvous::router(&config.prefix, sessions, max_bytes)
            .map_response(|res| res.map(|b| b.map_err(|e| anyhow!(e))));
        module_api.register_web_service(&config.prefix, service)?;
        Ok(Self)
    }

    #[staticmethod]
    fn parse_config(config: &PyAny) -> PyResult<Config> {
        parse_config(config)
    }
}

#[pymodule]
fn matrix_http_rendezvous_synapse(_py: Python, m: &PyModule) -> PyResult<()> {
    pyo3_log::init();

    m.add_class::<SynapseRendezvousModule>()?;
    Ok(())
}
