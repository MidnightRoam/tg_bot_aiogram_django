// Функция для создания элемента <li> сообщения
function createMessageLi(message) {
    const li = document.createElement('li');
    li.className = 'message__li';
    li.innerHTML = `
        <ul class='message__ul'>
            <li class="message__li">ID: ${message.id}</li>
            <li class="message__li">Message ID: ${message.message_id}</li>
            <li class="message__li">Дата сохранения: ${message.date}</li>
            <li class="message__li">Кому: ${message.to_whom}</li>
        </ul>
    `;
    return li;
}

// Функция для загрузки данных с сервера
function loadData() {
    fetch('/get_messages_list/')
        .then(response => response.json())
        .then(data => {
            const messagesList = document.getElementById('messages__ul');
            data.forEach(message => {
                const li = createMessageLi(message)
                messagesList.appendChild(li);
            });
        })
        .catch(error => console.error('Ошибка при получении данных:', error));
}

loadData();