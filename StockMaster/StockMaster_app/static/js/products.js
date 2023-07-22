var products = []

function handleAddProductForm(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    console.log('Form data:', Object.fromEntries(formData));
    const prd = {};
    formData.forEach((value, key) => {
        prd[key] = value;
    });
    var table_node = document.getElementById("products_table");
    var str = `<tr>
            <td>
            <a href="#" class="text-primary fw-bold">
            ${prd["p_name"]}
            </a>
            </td>
            <td>$${prd["cost"]}</td>
            <td class="fw-bold">${prd["qty"]}</td>
            <td>${prd["p_barcode"]}</td>
            <td>${prd["expire_date"]}</td>
            </tr>`;
    table_node.innerHTML += str;
    products.push(prd)
    event.target.reset();
}

function save_all_products() {
    $.ajax({
        url: 'http://localhost:8000/save_products/',
        type: "POST",
        data: products,
        dataType: "json",
        success: function (data) {
            let x = JSON.stringify(data);
            console.log(x);
        },
        error: function (error) {
            console.log(`Error ${error}`);
        }
    });
}