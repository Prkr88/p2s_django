$('.add_btn').click(function () {
    $(this).toggleClass('btn btn-success');
    $(this).toggleClass('btn btn-danger');
    let tr_id = '#'+$(this).closest('tr').attr('id'); // table row ID
    let index = $(tr_id).find('td:eq(0)').text();
    if($(this).text() === 'Add'){
        $(this).text("Remove");
        $(tr_id).css('background-color','#B2FBA7')
    }
    else{
        if (index%2 === 0){
            $(tr_id).css('background-color','#e9ecef');
        }
        else{
            $(tr_id).css('background-color','#dde0e3');
        }
        $(this).text("Add");
    }

});
