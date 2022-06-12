// Validaciones
$(document).ready(function () {
    $('#form-login').validate({
        rules: {
            username: {
                required: true,
                minlength: 5
            },
            password: {
                required: true,
                minlength: 5
            },
            confirm_password: {
                required: true,
                minlength: 5,
                equalTo: "#password"
            },
            agree: "required"
        },
        messages: {
            username: {
                required: "Por favor ingresa un usuario",
                minlength: "Tu usuario debe ser de no menos de 5 caracteres"
            },
            password: {
                required: "Por favor ingresa una contraseña",
                minlength: "Tu contraseña debe ser de no menos de 5 caracteres de longitud"
            },
        },
        errorElement: "em",
        errorPlacement: function (error, element) {
            error.addClass("help-block");

            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function (element, errorClass, validClass) {
            $(element).parents(".col-sm-10").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).parents(".col-sm-10").addClass("has-success").removeClass("has-error");
        }
    });
});