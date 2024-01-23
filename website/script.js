document.getElementById("message-form").addEventListener("submit", function(event) {
    event.preventDefault();
    var userInput = document.getElementById("user-input").value;
    document.getElementById("user-input").value = '';

    var newMessage = document.createElement("p");
    newMessage.textContent = userInput;
    newMessage.classList.add("user-message");
    document.getElementById("conversation").appendChild(newMessage);
});
