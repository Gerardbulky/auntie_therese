function sendMail(contactForm) {
    emailjs.send("gmail", "auntie_therese", {
        "from_name": contactForm.name.value,
        "from_message": contactForm.message.value
    })
        .then(function (response) {
            console.log('SUCCESS!', response.status, response.text);
        }, function (error) {
            console.log('FAILED...', error);
        });
}