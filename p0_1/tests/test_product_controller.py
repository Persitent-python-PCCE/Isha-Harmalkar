from unittest.mock import patch

import pytest

from controllers.productController import ProductController
from models.product import Product




@pytest.fixture
def product_controller():
    with patch("controllers.productController.ProductService") as MockProductService,\
        patch("controllers.productController.logger"):
        controller = ProductController()
        controller.mock_service = MockProductService.return_value
        yield controller

class TestProductController:
    @patch("builtins.input", side_effect=["1", "2", "Gaming Laptop", "999.99", "10", "Y"])
    def test_create_product_success(self, mock_input, product_controller):
        expected_product = Product(
            id=101,
            categoryId=1,
            supplierId=2,
            name="Gaming Laptop",
            unitPrice=999.99,
            stock=10,
            isActive=True
        )

        product_controller.mock_service.createProduct.return_value = expected_product
        result = product_controller.createProduct()

        assert result is not None
        assert result.id == 101
        assert result.name == "Gaming Laptop"
        product_controller.mock_service.createProduct.assert_called_once()


    @patch("builtins.input", side_effect=["101"])
    def test_get_product_by_id_success(self, mock_input, product_controller):
        expected_product = Product(
            id=101, categoryId=1, supplierId=2, name="Mouse", unitPrice=25.0, stock=50, isActive=True

        )

        product_controller.mock_service.getProduct.return_value = expected_product
        result = product_controller.getProductById()

        assert result is not None
        assert result.id == 101
        product_controller.mock_service.getProduct.assert_called_once_with(101)



    def test_get_all_products_success(self, product_controller):
        p1 = Product(id=1, categoryId=1, supplierId=1, name="P1", unitPrice=10.0, stock=5, isActive=True)
        p2 = Product(id=2, categoryId=1, supplierId=1, name="P2", unitPrice=20.0, stock=8, isActive=False)

        product_controller.mock_service.getAllProducts.return_value = [p1, p2]

        result = product_controller.getAllProducts()

        assert len(result) == 2
        assert result[0].id  == 1


    @patch("builtins.input", side_effect=["b"])
    def test_get_all_active_products_pagination_exit(self, mock_input, product_controller):
        p1 = Product(id=1, categoryId=1, supplierId=1, name="Active P1", unitPrice=10.0, stock=5, isActive=True)
        product_controller.mock_service.getAllActiveProducts.return_value = [p1]
        product_controller.getAllActiveProducts()
        product_controller.mock_service.getAllActiveProducts.assert_called_once_with(1, 5)


    @patch("builtins.input", side_effect=["101", "1", "2", "Updated Laptop", "1099.99", "15", "Y"])
    def test_update_product_success(self, mock_input, product_controller):
        product_controller.mock_service.updateProduct.return_value = True
        result = product_controller.updateProduct()
        assert result is True
        product_controller.mock_service.updateProduct.assert_called_once()

    @patch("builtins.input", side_effect=["101", "y"])
    def test_deactivate_product_success(self, mock_input, product_controller):
        product_controller.mock_service.deactivateProduct.return_value = True

        result = product_controller.deactivateProduct()
        assert result is True
        product_controller.mock_service.deactivateProduct.assert_called_once_with(101)


    @patch("builtins.input", side_effect=["101"])
    def test_activate_product_success(self, mock_input, product_controller):
        product_controller.mock_service.activateProduct.return_value = True

        result = product_controller.activateProduct()
        assert result is True

        product_controller.mock_service.activateProduct.assert_called_once_with(101)


    @patch("builtins.input", side_effect=["1", "2", "Invalid Price", "abc_not_a_float", "10", "Y"])
    def test_create_product_invalid_price_formate(self, mock_input, product_controller):
        result = product_controller.createProduct()
        assert result is None
        product_controller.mock_service.createProduct.assert_not_called()

    @patch("builtins.input", side_effect=["101", "n"])
    def test_deactivate_product_cancelled(self, mock_input, product_controller):
        result = product_controller.deactivateProduct()
        assert result is False
        product_controller.mock_service.deactivateProduct.assert_not_called()


    
