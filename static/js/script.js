document.addEventListener("DOMContentLoaded", function() {
    // Получаем форму и ее элементы
    const form = document.querySelector("form");
    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");

    // Добавляем обработчик события submit на форму
    form.addEventListener("submit", function(event) {
        // Проверяем, что все поля заполнены
        if (nameInput.value === "" || emailInput.value === "" || passwordInput.value === "") {
            alert("Все поля должны быть заполнены!");
            event.preventDefault();  // Предотвращаем отправку формы
        } else {
            alert("Форма отправлена успешно!");
            // Здесь можно добавить дополнительную обработку отправки формы, если необходимо
        }
    });
});