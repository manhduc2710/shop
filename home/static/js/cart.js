var vUpdateBtn = document.getElementsByClassName('update-cart')

for (i = 0; i < vUpdateBtn.length; i++) {
    vUpdateBtn[i].addEventListener('click', function() {
        var productId = this.dataset.product
        console.log(productId)
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)
        console.log('user', user)
        if (user === 'AnonymousUser') {
            alert('bạn chưa đăng nhập')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    var url = '/update_item/'
    fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then((response) => {
            return response.json
        })
        .then((data) => {
            location.reload()
        })
    
    
}

$(document).ready(function () {
    $('.incrementBtn').click(function (e) { 
        e.preventDefault();
        
        var inc_value = $(this).closest('.product_data').find('.quantity-input').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value) ? 0 : value;
        if (value < 10){
            value++;
            $(this).closest('.product_data').find('.quantity-input').val(value);
        }
    });


    $('.decrementBtn').click(function (e) { 
        e.preventDefault();
        
        var dec_value = $(this).closest('.product_data').find('.quantity-input').val();
        var value = parseInt(dec_value,10);
        value = isNaN(value) ? 0 : value;
        if (value > 1){
            value--;
            $(this).closest('.product_data').find('.quantity-input').val(value);
        }
    });


    $('.addtoCartBtn').click(function (e) { 
        e.preventDefault();
        
        var productId = $(this).closest('.product_data').find('.prod_id').val();
        var productquantity = $(this).closest('.product_data').find('.quantity-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'productId': productId,
                'productquantity': productquantity,
                csrfmiddlewaretoken: token
            },
            dataType: "dataType",
            success: function (response) {
                console.log(response)
                alertify.success(response.status)
            }
        });
    });
});
