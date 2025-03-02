async function sendQuery() {
    const prompt = document.getElementById("prompt").value;
    const responseBox = document.getElementById("response");
    const storyBox = document.getElementById("story");

    if (!prompt.trim()) {
        responseBox.innerText = "프롬프트를 입력하세요.";
        return;
    }

    responseBox.innerText = "응답을 기다리는 중...";
    storyBox.innerText = ""; // 기존 소설 결과 초기화

    try {
        const response = await fetch("/deepseek/query", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        responseBox.innerText = data.response || "오류 발생: " + data.error;

        if (data.response) {
            // 생성된 응답을 이용해 소설 생성 요청
            await translate_using_openai(data.response);
        }
    } catch (error) {
        responseBox.innerText = "네트워크 오류 발생";
    }
}

async function translate_using_openai(responseText) {
    const storyBox = document.getElementById("story");
    storyBox.innerText = "번역을 생성하는 중...";

    try {
        const response = await fetch("/openai/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: responseText, target_language: "Korean" })
        });

        const data = await response.json();
        storyBox.innerText = data.translated_text || "오류 발생: " + data.error;
    } catch (error) {
        storyBox.innerText = "네트워크 오류 발생";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.getElementById("prompt");
    const sendButton = document.getElementById("sendButton");

    sendButton.addEventListener("click", sendQuery);

    textarea.addEventListener("keydown", (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            sendButton.click();
        }
    });
});
