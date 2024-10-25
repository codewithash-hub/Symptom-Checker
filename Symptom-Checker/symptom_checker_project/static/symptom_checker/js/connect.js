function checkSymptoms() {
    $.post("/check_symptoms/", {
        symptoms: $("#symptoms").val(),
        csrfmiddlewaretoken: '{{ csrf_token }}'
    }, function(data) {
        $("#diagnosis").html(data.diagnosis);
    });
}

// Sidebar toggle functionality
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

function menuBtnChange() {
    closeBtn.classList.toggle("bx-menu-alt-right", sidebar.classList.contains("open"));
    closeBtn.classList.toggle("bx-menu", !sidebar.classList.contains("open"));
}

// Modal functionality
var modal = document.getElementById("contactModal");
var openModalBtn = document.getElementById("openModalBtn");
var closeModalBtn = document.getElementsByClassName("close")[0];

openModalBtn.addEventListener("click", () => modal.style.display = "block");
closeModalBtn.addEventListener("click", () => modal.style.display = "none");
window.addEventListener("click", (e) => {
    if (e.target == modal) modal.style.display = "none";
});

    // function getCookie(name) {
    //     let cookieValue = null;
    //     if (document.cookie && document.cookie !== '') {
    //         const cookies = document.cookie.split(';');
    //         for (let i = 0; i < cookies.length; i++) {
    //             const cookie = cookies[i].trim();
    //             if (cookie.substring(0, name.length + 1) === (name + '=')) {
    //                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    //                 break;
    //             }
    //         }
    //     }
    //     return cookieValue;
    // }

    // $.post("/check_symptoms/", {
    //     symptoms: $("#symptoms").val(),
    //     csrfmiddlewaretoken: getCookie('csrftoken')
    // }, function(data) {
    //     $("#diagnosis").html(data.diagnosis);
    // });


// function sendMessage() {
// const inputField = document.getElementById("symptoms");
// const message = inputField.value.trim();

// if (message) {
//     appendMessage("user-message", message);
//     inputField.value = "";

//     // Simulate bot response
//     setTimeout(() => {
//     appendMessage("ai-message", "This is an AI-generated response.");
//     }, 1000);
// }
// }

// function appendMessage(type, message) {
//     const chatBody = document.getElementById("chat-body");

//     const messageDiv = document.createElement("div");
//     messageDiv.classList.add("message", type);
    
//     const avatarDiv = document.createElement("div");
//     avatarDiv.classList.add(type === "user-message" ? "user-avatar" : "ai-avatar");

//     const avatarImg = document.createElement("img");
//     avatarImg.src = type === "user-message" ? "user-avatar.png" : "ai-avatar.png";
//     avatarDiv.appendChild(avatarImg);
    
//     const messageContentDiv = document.createElement("div");
//     messageContentDiv.classList.add("message-content");
    
//     const messageText = document.createElement("p");
//     messageText.textContent = message;
//     messageContentDiv.appendChild(messageText);

//     const timestampSpan = document.createElement("span");
//     timestampSpan.classList.add("timestamp");
//     timestampSpan.textContent = "Just now";
//     messageContentDiv.appendChild(timestampSpan);

//     messageDiv.appendChild(avatarDiv);
//     messageDiv.appendChild(messageContentDiv);

//     chatBody.appendChild(messageDiv);
//     chatBody.scrollTop = chatBody.scrollHeight;
//     }

function checkSymptoms() {
    const userMessage = $("#symptoms").val().trim();
    
    if (userMessage) {
        // Append user's message to the chat
        appendMessage("user-message", userMessage);
        $("#symptoms").val(""); // Clear the input field

        // Make the AJAX request to get AI response
        $.post("/check_symptoms/", {
            symptoms: userMessage,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        }, function(data) {
            // Append AI's response to the chat
            appendMessage("ai-message", data.diagnosis);
        });
    }
}

// Function to append messages to the chat area
function appendMessage(type, message) {
    const chatBody = document.getElementById("chat-body");

    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", type);
    
    const avatarDiv = document.createElement("div");
    avatarDiv.classList.add(type === "user-message" ? "user-avatar" : "ai-avatar");

    const avatarImg = document.createElement("img");
    avatarImg.src = type === "user-message" ? "user-avatar.png" : "ai-avatar.png";
    avatarDiv.appendChild(avatarImg);
    
    const messageContentDiv = document.createElement("div");
    messageContentDiv.classList.add("message-content");
    
    const messageText = document.createElement("p");
    messageText.textContent = message;
    messageContentDiv.appendChild(messageText);

    const timestampSpan = document.createElement("span");
    timestampSpan.classList.add("timestamp");
    timestampSpan.textContent = "Just now";
    messageContentDiv.appendChild(timestampSpan);

    messageDiv.appendChild(avatarDiv);
    messageDiv.appendChild(messageContentDiv);

    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight; // Scroll to the bottom
}


        // Get modal element
        var modal = document.getElementById("contactModal");
        var openModalBtn = document.getElementById("openModalBtn");
        var closeModalBtn = document.getElementsByClassName("close")[0];
    
        openModalBtn.addEventListener("click", openModal);
        closeBtn.addEventListener("click", closeModal);
        window.addEventListener("click", outsideClick);
    
        function openModal() {
        modal.style.display = "block";
        }
    
        function closeModal() {
        modal.style.display = "none";
        }
    
        function outsideClick(e) {
        if (e.target == modal) {
            modal.style.display = "none";
        }
    }