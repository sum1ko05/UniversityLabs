document.getElementById("myForm").addEventListener("submit", function(e) {
    const username = this.username.value;
    const email = this.email.value;
    const model = this.model.value;
    const amount = this.amount.value;
    const assembly_included = this.assembly_included.checked;
    const delivery = this.delivery.value

    // Only alert() on JS side
    alert(`Перепроверьте введённые данные:\n
            Ваше имя: ${username}\n
            Ваш email ${email}\n
            Выбранная модель: ${model}\n
            Количество заказанных моделей: ${amount}\n
            Включение сборки: ${assembly_included}\n
            Способ доставки: ${delivery}`);
});