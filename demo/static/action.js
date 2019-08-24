$(document).ready(function() {
    $('#register_form').on('submit', function(event) {

        $.ajax({
            Register_data : {
                register_name : $('#register_name').val(),
                register_email : $('#register_email').val(),
                register_password : $('#register_password').val()
            },
            type : 'POST',
            url : '/register_action'
        })
            .done(function(data) {

                if (Register_data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                }
                else {
                    $('#successAlert').text(data.name).show();
                    $('#errorAlert').hide();
                }

            });

        event.preventDefault();

    });

    $('#login_form').on('submit', function(event) {
        alert("Submitted");
        $.ajax({
            Login_data : {
                login_email : $('#login_email').val(),
                login_password : $('#login_password').val()
            },
            type : 'POST',
            url : '/login_action'
        })
            .done(function(data) {

                if (Login_data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                }
                else {
                    $('#successAlert').text(data.name).show();
                    $('#errorAlert').hide();
                }

            });
        event.preventDefault();
    });
});