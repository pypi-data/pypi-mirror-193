use pyo3::prelude::*;
use ndarray::Array2;

use numpy::ndarray::{ArrayD, ArrayViewD, ArrayViewMutD};
use numpy::{IntoPyArray, PyArrayDyn, PyReadonlyArrayDyn, PyReadonlyArray2};

#[pyfunction()]
#[pyo3(signature = (line_points, point_cloud, parallel = false))]
/// For every point in ``point_cloud``, find it's nearest neighbor in ``line_points``
///
/// :param np.ndarray line_points: a 2D numpy array with each point being described by a row, and columns of coordinates of that point. Array should be in the shape ``(NUM_LINE_POINTS, 2)``
/// :param np.ndarray point_cloud: a 2D numpy array with each point being described by a row, and columns of coordinates of that point. Array should be in the shape ``(NUM_POINT_CLOUD_POINTS, 2)``
/// :param bool parallel: enable parallel processing for the dataset. If you have more than 2,000 line points and 2,000 point cloud points this may be useful.
///
/// this function returns a list of indicies of size ``NUM_POINT_CLOUD_POINTS``, where every index
/// in the list is the index of the ``line_points`` row that is closest to the ``point_cloud``
/// point.
///
/// Example:
///
/// .. code-block::
///     
///     import toha_nearest_neighbor
///     import numpy as np
///
///     line_points = np.array(
///         [
///             [0.0, 0.0],
///             [1.0, 1.0],
///             [2.0, 2.0],
///         ]
///     )
///
///     point_cloud = np.array(
///         [
///             [0.1, -0.1], #closest to the 0-th index of line_points rows
///             [2.2, 3.0], # closest to the 2-nd index of line_points rows
///         ]
///     )
///
///     # output: [0, 2]
///     toha_nearest_neighbor.brute_force(line_points, point_cloud)
fn brute_force(
    line_points: PyReadonlyArray2<'_, f64>,
    point_cloud: PyReadonlyArray2<'_, f64>,
    parallel: bool
) -> Vec<usize> {

    if parallel {
        super::brute_force_par(line_points.as_array(), point_cloud.as_array())
    } else {
        super::brute_force(line_points.as_array(), point_cloud.as_array())
    }
}

/// This module is implemented in Rust.
#[pymodule]
fn toha_nearest_neighbor(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(brute_force, m)?)?;
    Ok(())
}
