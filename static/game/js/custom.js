$('#truecallerBtn').click(function () {
    mobile = $('#txtMobile').val();
    var infoModal = $('#myModal');
    var url = "http://127.0.0.1:8000/api/truecaller/?mobile="+mobile;
    $.ajax({url: url, type: "post", success: function (result) {


        var htmlData = ' <div class="form-group">';
        htmlData += '<label for="forName" style="float: left; color: black;">Name</label>';
        htmlData += '<input type="text" class="form-control" id="txtModalName" value="'+result.name+'">';
        htmlData += '<label for="forGender" style="float: left; color: black;">Gender</label>';
        htmlData += '<input type="text" class="form-control" id="txtModalGender" value="'+result.gender+'">';
        htmlData += '<label for="forEmail" style="float: left; color: black;">Email</label>';
        htmlData += '<input type="text" class="form-control" id="txtModalEmail" value="'+result.email+'">';
        htmlData += '<label for="forArea" style="float: left; color: black;">Area</label>';
        htmlData += '<input type="text" class="form-control" id="txtModalArea" value="'+result.area+'">';
        htmlData += '<input type="hidden" class="form-control" id="txtModalId" value="'+result.id+'">';
        htmlData += '</div>';

        infoModal.find('#modal-body')[0].innerHTML = htmlData;
        infoModal.modal();
    }});
});

$('#modalSet').click(function () {
    var id = $('#txtModalId').val();
    var name = $('#txtModalName').val();
    var gender = $('#txtModalGender').val();
    var email = $('#txtModalEmail').val();
    var area = $('#txtModalArea').val();
    var data = {
        'name': name,
        'gender': gender,
        'email': email,
        'area': area
    };
    var url = "http://127.0.0.1:8000/api/truecaller/"+id+"/";
    $.ajax({
        url: url,
        type: "put",
        data: data,
        success: function (result) {

            $('#myModal').modal('toggle');
            $('.alert').css("display", "block");
            location.reload();

        }
    });

});


