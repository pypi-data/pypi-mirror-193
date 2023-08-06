#![allow(non_snake_case)]
use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;

mod types;

#[cfg(not(target_family = "windows"))]
mod linux;
#[cfg(not(target_family = "windows"))]
use linux::{linux_ifaddresses as ifaddresses, linux_interfaces as interfaces};

#[cfg(target_family = "windows")]
mod win;
#[cfg(target_family = "windows")]
use win::{windows_ifaddresses as ifaddresses, windows_interfaces as interfaces};

pub fn ip_to_string(ip: u32) -> String {
    let mut s = String::new();

    for i in 0_u8..4 {
        let grp_idx = 4 - i - 1;
        let group_val = (ip >> (grp_idx * 8)) & 0xFF;

        let sep = if i < 3 { "." } else { "" };

        let formatted = format!("{group_val}{sep}");
        s.push_str(&formatted);
    }

    s
}

#[pyfunction]
pub fn _ip_to_string(ip: u32) -> String {
    ip_to_string(ip)
}

#[pyfunction]
fn _interfaces() -> PyResult<Vec<String>> {
    let maybe_ifs = interfaces();

    maybe_ifs.map_err(|e| {
        let str_message = e.to_string();
        PyErr::new::<PyRuntimeError, _>(str_message)
    })
}

#[pyfunction]
fn _ifaddresses(if_name: &str) -> PyResult<types::IfAddrs> {
    let maybe_ifaddrs = ifaddresses(if_name);

    maybe_ifaddrs.map_err(|e| {
        let str_message = e.to_string();
        PyErr::new::<PyRuntimeError, _>(str_message)
    })
}

#[pymodule]
fn netifaces(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(_interfaces, m)?)?;
    m.add_function(wrap_pyfunction!(_ifaddresses, m)?)?;
    m.add_function(wrap_pyfunction!(_ip_to_string, m)?)?;
    Ok(())
}
