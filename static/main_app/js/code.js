// ADD REMOVE UI Function
function editTableLine(button) {
    $(button).toggleClass('btn btn-success');
    $(button).toggleClass('btn btn-danger');
    let tr_id = '#' + $(button).closest('tr').attr('id'); // table row ID
    let index = $(tr_id).find('td:eq(0)').text();
    let btn_txt = $(button).text();
    if (btn_txt === 'Add') {
        $(button).text("Remove");
        $(tr_id).css('background-color', '#B2FBA7')
    }
    else {
        if (index % 2 === 0) {
            $(tr_id).css('background-color', '#e9ecef');
        }
        else {
            $(tr_id).css('background-color', '#dde0e3');
        }
        $(button).text("Add");
    }

}

let prev_color;
$(".fleet_tbl_row").mouseenter(function () {
    prev_color = $(this).css('background-color');
    $(this).css('background-color', 'rgb(178,251,167)');
}).mouseleave(function () {
    $(this).css('background-color', prev_color);
});

let d = new Date();
let month = d.getMonth() + 1;
let day = d.getDate();

let output = (day < 10 ? '0' : '') + day + '/' +
    (month < 10 ? '0' : '') + month + '/' +
    d.getFullYear();
$('.date').text(output);


// using jQuery
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//ADD TO CART AJAX
$('.add_btn').click(function (e) {
    e.preventDefault();
    let csrftoken = getCookie('csrftoken');
    // alert(token);
    let qty = $(this).closest('tr').find('.qty_selector').val();
    let button_ref = $(this);
    let mode = $(button_ref).text();
    if (qty > 0) {
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            type: "POST",
            url: "../add_to_cart/",
            // dataType: 'json',
            data: {
                "item_id": $(this).attr('id'),
                "qty": qty,
                "mode": mode,
            },
            success: function (result) {
                // let tr_id = '#' + $(button_ref).closest('tr').attr('id');
                editTableLine(button_ref);
                let tr_id = '#' + $(button_ref).closest('tr').attr('id'); // table row ID
                let item_name = $(tr_id).find('td:eq(1)').text();
                let opp = '';
                if (mode === 'Add') {
                    opp = ' added to Cart';
                    $('#view_cart').css('display','inline')
                }
                else {
                    opp = ' removed from Cart';
                }
                alert(item_name + ' X ' + qty + opp);
            },
            error: function (result) {
                alert('error');
            }
        });
    } else {
        alert("qty>0")
    }
});

