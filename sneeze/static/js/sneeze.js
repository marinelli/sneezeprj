
$(function() {

    var loadForm = function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#modal-entity").modal("show");
            },
            success: function(data) {
                $("#modal-entity .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function() {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#entity-table tbody").html(data.html_list);
                    $("#modal-entity").modal("hide");
                } else {
                    $("#modal-entity .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    // Create an entity
    $(".js-create-entity").click(loadForm);
    $("#modal-entity").on("submit", ".js-entity-create-form", saveForm);

    // Update an entity
    $("#entity-table").on("click", ".js-update-entity", loadForm);
    $("#modal-entity").on("submit", ".js-entity-update-form", saveForm);

    // Delete an entity
    $("#entity-table").on("click", ".js-delete-entity", loadForm);
    $("#modal-entity").on("submit", ".js-entity-delete-form", saveForm);

});

