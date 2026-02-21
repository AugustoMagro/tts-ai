async function GetAudio() {
  const formData = new FormData();

  const texto = document.getElementById("texto-input").value
  const voice = document.getElementById("voices").value

  const bt_gerar_fala = document.getElementById("bt-gerar-fala")
  bt_gerar_fala.textContent = "Aguardando"

  try { 
    const res = await fetch('/api/audio', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ texto, voice}),
    });
    if (!res.ok) {
      const data = await res.json();
      throw new Error(`Failed to get videos. Error: ${data.error}`);
    }

    const blob = await res.blob();
    const objectURL = URL.createObjectURL(blob);

    file = document.getElementById("audio-file");
    file.href = objectURL;
    file.download = objectURL;
    file.click();

  } catch (error) {
    alert(`Error: ${error.message}`);
  } finally {
    bt_gerar_fala.textContent = "Gerar Fala"
  }
}
