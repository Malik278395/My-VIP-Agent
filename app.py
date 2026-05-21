rm app.py
cat << 'EOF' > app.py
from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyAOOZ-WTB7xdmNfCgf-puFkFc11W8SFCWk"

# 🌟 AGENT NAME: Aap yahan "MY VIP AGENT" ki jagah apna pasandida naam likh sakte hain
BOT_NAME = "MY VIP AGENT"

HTML_CODE = """
<!DOCTYPE html>
<html lang="ur">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ """ + BOT_NAME + """ VIP AI ⚡</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #e2e8f0; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        
        #chat-container { width: 100%; max-width: 600px; height: 95vh; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(16px); border-radius: 24px; border: 1px solid rgba(255,255,255,0.1); display: flex; flex-direction: column; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); margin: 10px; }
        
        .chat-header { padding: 20px; background: rgba(15, 23, 42, 0.6); border-bottom: 1px solid rgba(255,255,255,0.05); border-top-left-radius: 24px; border-top-right-radius: 24px; display: flex; align-items: center; justify-content: space-between; }
        .header-left { display: flex; align-items: center; gap: 15px; }
        .avatar { width: 45px; height: 45px; background: linear-gradient(45deg, #ec4899, #8b5cf6); border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 20px; box-shadow: 0 0 15px rgba(236, 72, 153, 0.5); }
        .header-info h2 { font-size: 18px; font-weight: 600; color: #fff; letter-spacing: 0.5px; }
        .header-info p { font-size: 12px; color: #10b981; display: flex; align-items: center; gap: 5px; }
        .header-info p::before { content: ''; width: 8px; height: 8px; background: #10b981; border-radius: 50%; display: inline-block; box-shadow: 0 0 8px #10b981; }

        .voice-controls { display: flex; gap: 10px; }
        .mute-btn { background: rgba(255,255,255,0.1); border: none; color: white; width: 35px; height: 35px; border-radius: 50%; cursor: pointer; display: flex; justify-content: center; align-items: center; transition: 0.2s; }
        .mute-btn.active { background: #ef4444; }

        #messages-body { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 15px; scroll-behavior: smooth; }
        #messages-body::-webkit-scrollbar { width: 6px; }
        #messages-body::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 10px; }
        
        .msg-wrapper { display: flex; width: 100%; flex-direction: column; }
        .msg-wrapper.user-wrapper { align-items: flex-end; }
        .msg-wrapper.ai-wrapper { align-items: flex-start; }

        .bubble { max-width: 80%; padding: 14px 18px; border-radius: 18px; font-size: 15px; line-height: 1.6; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); word-wrap: break-word; }
        .user-wrapper .bubble { background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: white; border-bottom-right-radius: 4px; }
        .ai-wrapper .bubble { background: rgba(51, 65, 85, 0.8); color: #f1f5f9; border-bottom-left-radius: 4px; border: 1px solid rgba(255,255,255,0.05); }
        
        .msg-meta { font-size: 11px; color: #64748b; margin-top: 4px; padding: 0 5px; }

        .chat-input-area { padding: 15px 20px; background: rgba(15, 23, 42, 0.4); border-top: 1px solid rgba(255,255,255,0.05); border-bottom-left-radius: 24px; border-bottom-right-radius: 24px; display: flex; gap: 12px; align-items: center; }
        .input-wrapper { flex: 1; position: relative; background: #334155; border-radius: 14px; border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; padding: 0 15px; }
        
        input[type="text"] { width: 100%; background: transparent; border: none; padding: 14px 0; color: white; font-size: 15px; outline: none; }
        input[type="text"]::placeholder { color: #94a3b8; }
        
        .action-btn { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); color: white; border: none; width: 48px; height: 48px; border-radius: 14px; cursor: pointer; display: flex; justify-content: center; align-items: center; font-size: 18px; transition: all 0.2s ease; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); }
        .action-btn:hover { transform: translateY(-2px); }
        #micBtn { background: linear-gradient(135deg, #ec4899 0%, #d946ef 100%); box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3); }
        #micBtn.listening { background: #ef4444; animation: pulse 1.5s infinite; }

        @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.08); } 100% { transform: scale(1); } }

        .welcome-screen { text-align: center; margin: auto; max-width: 80%; padding: 20px; }
        .welcome-screen i { font-size: 50px; background: linear-gradient(45deg, #ec4899, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 15px; }
        .welcome-screen h3 { font-size: 20px; margin-bottom: 8px; color: #fff; }
        
        .typing-dots span { width: 8px; height: 8px; background: #94a3b8; border-radius: 50%; display: inline-block; animation: bounce 1.3s infinite ease-in-out; }
        .typing-dots span:nth-child(2) { animation-delay: 0.15s; }
        .typing-dots span:nth-child(3) { animation-delay: 0.3s; }
        @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
    </style>
</head>
<body>

    <div id="chat-container">
        <div class="chat-header">
            <div class="header-left">
                <div class="avatar"><i class="fa-solid fa-headset"></i></div>
                <div class="header-info">
                    <h2>""" + BOT_NAME + """</h2>
                    <p>Voice Call Active</p>
                </div>
            </div>
            <div class="voice-controls">
                <button class="mute-btn" id="audioToggle" onclick="toggleAudio()" title="AI Voice On/Off"><i class="fa-solid fa-volume-high"></i></button>
            </div>
        </div>

        <div id="messages-body">
            <div class="welcome-screen" id="welcome">
                <i class="fa-solid fa-microphone-lines"></i>
                <h3>Boliye, Main Sun Raha Hoon!</h3>
                <p>Aap nichi diye gaye Pink Mic icon ko daba kar mujhse bol kar baat kar sakte hain.</p>
            </div>
        </div>

        <div class="chat-input-area">
            <button class="action-btn" id="micBtn" onclick="startSpeechRecognition()" title="Bol kar baat karein"><i class="fa-solid fa-microphone"></i></button>
            <div class="input-wrapper">
                <input type="text" id="userInput" placeholder="Type karein ya mic dabayein..." onkeypress="if(event.key === 'Enter') sendMessage()">
            </div>
            <button class="action-btn" onclick="sendMessage()"><i class="fa-solid fa-paper-plane"></i></button>
        </div>
    </div>

    <script>
        let isVoiceEnabled = true;
        let currentAudioSource = null;

        function toggleAudio() {
            isVoiceEnabled = !isVoiceEnabled;
            let btn = document.getElementById("audioToggle");
            if(isVoiceEnabled) {
                btn.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
                btn.classList.remove("active");
            } else {
                btn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
                btn.classList.add("active");
                if(window.speechSynthesis) window.speechSynthesis.cancel();
            }
        }

        // 🎙️ Voice Input (Speech to Text)
        function startSpeechRecognition() {
            window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!window.SpeechRecognition) {
                alert("Aapka browser voice input support nahi karta. Chrome use karein.");
                return;
            }

            const recognition = new SpeechRecognition();
            recognition.interimResults = false;
            recognition.lang = 'en-US'; // Roman Urdu/Hindi ke liye English script best kaam karti hai

            const micBtn = document.getElementById("micBtn");
            micBtn.classList.add("listening");

            recognition.start();

            recognition.onresult = (event) => {
                const speechToText = event.results[0][0].transcript;
                document.getElementById("userInput").value = speechToText;
                sendMessage();
            };

            recognition.onerror = (err) => {
                console.error(err);
                micBtn.classList.remove("listening");
            };

            recognition.onend = () => {
                micBtn.classList.remove("listening");
            };
        }

        // 🔊 AI Voice Output (Text to Speech)
        function speakText(text) {
            if (!isVoiceEnabled) return;
            if (window.speechSynthesis) {
                window.speechSynthesis.cancel(); // Purani aawaz rokein
                
                // Markdown/Stars saaf karne ke liye
                let cleanText = text.replace(/[*#_]/g, "");
                
                const utterance = new SpeechSynthesisUtterance(cleanText);
                utterance.lang = 'hi-IN'; // Urdu/Hindi accent ke liye perfect voice pitch
                utterance.rate = 1.0;
                window.speechSynthesis.speak(utterance);
            }
        }

        async function sendMessage() {
            let input = document.getElementById("userInput");
            let body = document.getElementById("messages-body");
            let welcome = document.getElementById("welcome");
            
            if (!input.value.trim()) return;
            
            if (welcome) welcome.remove();
            
            let text = input.value;
            input.value = "";
            
            let time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
            body.innerHTML += `
                <div class="msg-wrapper user-wrapper">
                    <div class="bubble">${text}</div>
                    <div class="msg-meta">Tum • ${time}</div>
                </div>
            `;
            body.scrollTop = body.scrollHeight;
            
            let loadingId = "load-" + Date.now();
            body.innerHTML += `
                <div class="msg-wrapper ai-wrapper" id="${loadingId}">
                    <div class="bubble typing-dots">
                        <span></span> <span></span> <span></span>
                    </div>
                </div>
            `;
            body.scrollTop = body.scrollHeight;
            
            try {
                let res = await fetch("/get?msg=" + encodeURIComponent(text));
                let data = await res.text();
                
                document.getElementById(loadingId).remove();
                
                body.innerHTML += `
                    <div class="msg-wrapper ai-wrapper">
                        <div class="bubble">${data.replace(/\\n/g, '<br>')}</div>
                        <div class="msg-meta">""" + BOT_NAME + """ • ${time}</div>
                    </div>
                `;
                
                // AI bolna shuru karega
                speakText(data);
                
            } catch (err) {
                document.getElementById(loadingId).remove();
                body.innerHTML += `
                    <div class="msg-wrapper ai-wrapper">
                        <div class="bubble" style="color:#ef4444; background:rgba(239,68,68,0.1);">Connection Error!</div>
                    </div>
                `;
            }
            body.scrollTop = body.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_CODE)

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": user_text}]}]
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        response_data = response.json()
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            return response_data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "Maaf kijiyega, server busy hai."
    except Exception as e:
        return f"System Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
EOF
python app.py
