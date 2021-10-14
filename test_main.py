# -*- coding: utf-8 -*-
from main import covariance, eig, pca
import unittest
import numpy as np

class TestCase(unittest.TestCase):

    def assertAllClose(self, a, b, rtol=1e-5, atol=1e-8):
        self.assertTrue(np.allclose(a, b, rtol=rtol, atol=atol))

    def test_covariance(self):
        self.assertAllClose(covariance(np.array([[1., 1.],
                                                 [1., -1.],
                                                 [-1., 1.],
                                                 [-1., -1.]])),
                            np.identity(2))

    def test_eig(self):
        def _inner_test(A):
            dim = A.shape[0]
            eig_val_array, eig_vec_array = eig(A)
            self.assertAllClose(np.sort(eig_val_array), eig_val_array)
            self.assertAllClose(eig_vec_array.T @ eig_vec_array, np.identity(dim))
            self.assertAllClose(A @ eig_vec_array, eig_val_array * eig_vec_array)
            pass

        _inner_test(np.identity(10))
        for _ in range(10):
            A = np.random.randn(10, 10)
            A = A + A.T
            _inner_test(A)
        
    def test_pca(self):
        n_examples = 100
        dim = 10
        n_components = 5
        X = np.random.randn(n_examples, dim)
        X[:, 0] = 10 * X[:, 0]
        Z, U = pca(X, n_components)
        self.assertEqual(Z.shape, (n_examples, n_components))
        self.assertEqual(U.shape, (n_components, dim))
        self.assertAllClose(U @ U.T,
                            np.identity(n_components))
        eig_vec = np.zeros(dim)
        eig_vec[0] = 1.0
        self.assertAllClose(U[-1],
                            eig_vec, atol=1e-1)

if __name__ == "__main__":
    unittest.main()
