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
        const response = await fetch("/openai/query", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        responseBox.innerText = data.response || "오류 발생: " + data.error;

        if (data.response) {
            // 생성된 응답을 이용해 소설 생성 요청
            await generateStory(data.response);
        }
    } catch (error) {
        responseBox.innerText = "네트워크 오류 발생";
    }
}

async function generateStory(responseText) {
    const storyBox = document.getElementById("story");
    storyBox.innerText = "소설을 생성하는 중...";

    try {
        const response = await fetch("/openai/generate_story", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: responseText })
        });

        const data = await response.json();
        storyBox.innerText = data.story || "오류 발생: " + data.error;
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
