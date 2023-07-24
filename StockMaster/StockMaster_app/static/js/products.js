
var products = [];
var productId = 0;

function handleAddProductForm(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const prd = {};
    formData.forEach((value, key) => {
        prd[key] = value;
    });

    prd['id'] = productId;
    productId++;

    var table_node = document.getElementById("products_table").getElementsByTagName('tbody')[0];
    var str = `<tr data-product-id="${prd['id']}">
                <td>${prd["p_name"]}</td>
                <td>${prd["cost"]}</td>
                <td class="fw-bold">${prd["qty"]}</td>
                <td>${prd["p_barcode"]}</td>
                <td>${prd["expire_date"]}</td>
                <td><a href="#" class="text-primary fw-bold" onclick="removeProduct(event)">
                Remove
                </a></td>
                </tr>`;
    table_node.innerHTML += str;
    products.push(prd)
    event.target.reset();
}

function removeProduct(event) {
    var row = event.target.closest('tr'); //this line finds the closest tr
    var productId = parseInt(row.dataset.productId);
    var productIndex = products.findIndex(product => product.id === productId);
    if (productIndex !== -1) {
        products.splice(productIndex, 1);
        row.remove();
    }
}

function save_all_products() {
    var data = JSON.stringify(products);
    console.log('Data received:', data);
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var saveUrl = saveProductsUrl;
    var validationErrors = validateProducts(products);
    if (validationErrors.length > 0) {
        alert('Validation failed. Please check the form fields.');
        return;
    }

    $.ajax({
        url: saveUrl,
        type: 'POST',
        data: {
            'data': data,
            'csrfmiddlewaretoken': csrfToken,
        },
        dataType: 'json',
        success: function (response) {
            console.log('Save successful:', response);
            alert('Products saved successfully');
            clearForm();
        },
        Error: function (response) {
            console.log('Error', response);
            alert('Error');
        },
    });
}

function clearForm() {
    $('#products').empty();
}

function validateProducts(products) {
    var errors = [];

    // Loop through each product and perform validations
    for (var i = 0; i < products.length; i++) {
        var product = products[i];

        // Perform basic validations for each product
        if (!product.p_name) {
            errors.push('Product name is required.');
        }

        if (!product.p_barcode || isNaN(parseInt(product.p_barcode))) {
            errors.push('Invalid barcode value for product.');
        }

        if (!product.expire_date) {
            errors.push('Expiry date is required for product.');
        }

        if (!product.cost || isNaN(parseFloat(product.cost))) {
            errors.push('Invalid cost value for product.');
        }

        if (!product.qty || isNaN(parseInt(product.qty))) {
            errors.push('Invalid quantity value for product.');
        }
    }

    return errors;
}
