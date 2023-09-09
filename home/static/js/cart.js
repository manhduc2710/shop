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

function active_course() {
    if ($(".active_course").length) {
      $(".active_course").owlCarousel({
        loop: true,
        margin: 20,
        items: 3,
        nav: true,
        autoplay: 2500,
        smartSpeed: 1500,
        dots: false,
        responsiveClass: true,
        thumbs: true,
        thumbsPrerendered: true,
        navText: ["<img src='https://colorlib.com/preview/theme/edustage/img/prev.png'>", "<img src='https://colorlib.com/preview/theme/edustage/img/next.png'>"],
        responsive: {
          0: {
            items: 1,
            margin: 0
          },
          991: {
            items: 2,
            margin: 30
          },
          1200: {
            items: 3,
            margin: 30
          }
        }
      });
    }
  }
  active_course(); 