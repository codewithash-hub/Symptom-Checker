function checkSymptoms() {
    $.post("/check_symptoms/", {
        symptoms: $("#symptoms").val(),
        csrfmiddlewaretoken: '{{ csrf_token }}'
    }, function(data) {
        $("#diagnosis").html(data.diagnosis);
    });
}

