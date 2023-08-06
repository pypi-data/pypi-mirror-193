extern crate bliss_audio as original_bliss;
use original_bliss::Song as BlissSong;
use pyo3::prelude::*;

#[pyclass]
pub struct Song {
    inner: BlissSong,
}

#[pymethods]
// TODO with syntax?
// TODO exceptions ?
impl Song {
    #[getter]
    fn title(&self) -> Option<String> {
        self.inner.title.to_owned()
    }

    #[getter]
    fn path(&self) -> String {
        self.inner.path.to_owned().to_string_lossy().to_string()
    }

    #[getter]
    fn artist(&self) -> Option<String> {
        self.inner.artist.to_owned()
    }

    #[getter]
    fn album(&self) -> Option<String> {
        self.inner.album.to_owned()
    }

    #[getter]
    fn track_number(&self) -> Option<String> {
        self.inner.track_number.to_owned()
    }

    #[getter]
    fn genre(&self) -> Option<String> {
        self.inner.genre.to_owned()
    }

    #[getter]
    fn analysis(&self) -> Vec<f32> {
        self.inner.analysis.as_vec()
    }

    #[new]
    fn new(path: &str) -> Self {
        Song {
            inner: BlissSong::from_path(path).unwrap(),
        }
    }
}

#[pymodule]
fn bliss_audio(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Song>()?;

    Ok(())
}
