from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='zh-TW')
    filename = 'CasperTestingAndroidRootTaiwan.mp3'
    tts.save(filename)

speak("香港01是一家互聯網企業，核心業務為倡議型媒體，主要傳播平台是手機應用程式和網站。企業研發各種互動數碼平台，開發由知識與科技帶動的多元化生活。")