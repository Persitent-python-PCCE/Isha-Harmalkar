from controllers.supplierController import SupplierController
import pytest
from unittest.mock import patch
from models.supplier import Supplier




@pytest.fixture
def supplier_controller():
    #mock supplier service
    with patch("controllers.supplierController.SupplierService") as MockSupplierService:
        controller = SupplierController()
        controller.mock_service = MockSupplierService.return_value
        yield controller


class TestSupplierController:

    @patch("builtins.input", side_effect=["Acme Corp", "John Smith", "Manager", "New York", "+1234567890"])
    def test_create_supplier_success(self, mock_input, supplier_controller):
        expected_supplier  = Supplier(
            id=1,
            companyName="Acme Corp",
            contactName="John Smith",
            contactDesignation="Manager",
            city="New York",
            contactNo="+1234567890"

        )

        supplier_controller.mock_service.createSupplier.return_value  = expected_supplier

        result = supplier_controller.createSupplier()


        assert result is not None
        assert result.id == 1
        assert result.companyName == "Acme Corp"
        supplier_controller.mock_service.createSupplier.assert_called_once()



    @patch("builtins.input", side_effect=["10"])
    def test_get_supplier_by_id_success(self, mock_input, supplier_controller):
        expected_supplier = Supplier(
            id=10,
            companyName="Tech Supplies",
            contactName="Alice",
            contactDesignation="Sales",
            city="Boston",
            contactNo=+915874962253
        )

        supplier_controller.mock_service.getSupplierById.return_value = expected_supplier

        result = supplier_controller.getSupplierById()

        assert result is not None
        assert result.id == 10
       
        supplier_controller.mock_service.getSupplierById.assert_called_once_with(10)


    def test_get_all_suppliers_success(self, supplier_controller):
        s1 = Supplier(id=1, companyName="A", contactName="B", contactDesignation="C", city="D", contactNo="124134")
        s2 = Supplier(id=2, companyName="Z", contactDesignation="L", contactName="JK", city="S", contactNo="9+85623")

        supplier_controller.mock_service.getAllSuppliers.return_value = [s1, s2]

        result = supplier_controller.getAllSuppliers()

        assert len(result) == 2
        assert result[0].id == 1

    @patch("builtins.input", side_effect=["1", "Updated INC", "Jane Doe", "CEO", "Chicago", "45879612563"])
    def test_update_supplier_success(self, mock_input, supplier_controller):
        supplier_controller.mock_service.updateSupplier.return_value = True

        result = supplier_controller.updateSupplier()

        assert result is True

        supplier_controller.mock_service.updateSupplier.assert_called_once()

    @patch("builtins.input", side_effect=["invalid_id"])

    def test_get_supplier_by_id_invalid_format(self, mock_input, supplier_controller):
        result = supplier_controller.getSupplierById()
        assert result is None
        supplier_controller.mock_service.getSupploerById.assert_not_called()

    @patch("builtins.input", side_effect=["1", "yes"])
    def test_delete_supplier_foreign_key_restrict(self, mock_input, supplier_controller):
        supplier_controller.mock_service.deleteSupplier.side_effect = ValueError(
            "Cannot delete supplier referenced by active products"
        )

        result = supplier_controller.deleteSupplier()
        assert result is False

    @patch("builtins.input", side_effect=["invalid_id"])
    def test_get_supplier_by_id_invalid_format(self, mock_input, supplier_controller):
        result = supplier_controller.getSupplierById()
        assert result is None

        supplier_controller.mock_service.getSupplierById.assert_not_called()


    @patch("builtins.input", side_effect=["1", "no"])
    def test_delete_supplier_cancelled_by_user(self, mock_input, supplier_controller):
        result = supplier_controller.deleteSupplier()

        assert result is False
        supplier_controller.mock_service.deleteSupplier.assert_not_called()

    @patch("builtins.input", side_effect=["1", "yes"])
    def test_delete_supplier_success(self, mock_input, supplier_controller):
        supplier_controller.mock_service.deleteSupplier.return_value = True
        result = supplier_controller.deleteSupplier()
        assert result is True

        supplier_controller.mock_service.deleteSupplier.assert_called_once_with(1)
        


    

           