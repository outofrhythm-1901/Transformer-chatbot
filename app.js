const form = document.querySelector("#chat-form");
const input = document.querySelector("#message-input");
const messages = document.querySelector("#messages");
const sendButton = document.querySelector("#send-button");

function addMessage(text, role) {
  const wrapper = document.createElement("div");
  wrapper.className = `message ${role}`;

  const label = document.createElement("span");
  label.className = "speaker";
  label.textContent = role === "user" ? "YOU" : "BOT";

  const paragraph = document.createElement("p");
  // textContent prevents user/API text from being interpreted as HTML.
  paragraph.textContent = text;

  wrapper.append(label, paragraph);
  messages.appendChild(wrapper);
  messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";
  input.focus();
  sendButton.disabled = true;
  sendButton.textContent = "Thinking…";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const data = await response.json();

    if (!response.ok || !data.success) {
      throw new Error(data.error || "The request could not be completed.");
    }
    addMessage(data.reply, "bot");
  } catch (error) {
    addMessage(`Sorry, I couldn't reach the server. ${error.message}`, "bot");
  } finally {
    sendButton.disabled = false;
    sendButton.innerHTML = 'Send <span aria-hidden="true">↗</span>';
  }
});
