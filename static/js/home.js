async function GetAudio() {
  const formData = new FormData();

  const texto = document.getElementById("input-texto").value
  const voice = document.getElementById("voices").value

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
  }
}
