

var subject = document.getElementById("subject").text;
console.log("subject :",subject)
var input = document.getElementById("question");

input.addEventListener("keyup", function (event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("text-send").click();
    }
});


var audio = document.querySelector('#audioe');

function captureMicrophone(callback) {
    navigator.getUserMedia = navigator.getUserMedia || navigator.mozGetUserMedia || navigator.webkitGetUserMedia;
    navigator.getUserMedia({audio: true}, callback, function (error) {
        alert('Unable to access your microphone.');
        console.error(error);
    });
}

function stopRecordingCallback() {
    audio.src = audio.srcObject = null;
    var blob = recorder.getBlob();
    audio.src = URL.createObjectURL(blob);
    document.getElementById('audioe').style.display='block';
    document.getElementById('text-send').style.display='none';
    document.getElementById('audio_send').style.display='block';
    audio.volume = 1;
    recorder.microphone.stop();

}

var recorder; // globally accessible
document.getElementById('start-recording').onclick = function () {
    this.style.display='none';
    document.getElementById('stop-recording').style.display='block';
    captureMicrophone(function (microphone) {
        audio.volume = 0
        audio.srcObject = microphone
        recorder = RecordRTC(microphone, {
            type: 'audio/wav',
            recorderType: StereoAudioRecorder,
            numberOfAudioChannels: 1, // or leftChannel:true
            desiredSampRate: 16000
        });
        recorder.startRecording();
        // release microphone on stopRecording
        recorder.microphone = microphone;
        });
    };

document.getElementById('stop-recording').onclick = function () {
    this.style.display='none';
    document.getElementById('trash-recording').style.display='block';
    recorder.stopRecording(stopRecordingCallback);
};

document.getElementById('trash-recording').onclick = function () {
    this.style.display='none';
    document.getElementById('start-recording').style.display='block';
    document.getElementById('audioe').style.display='none';
    document.getElementById('text-send').style.display='block';
    document.getElementById('audio_send').style.display='none';
    recorder = null;
};





$('#communication').scrollTop($('#communication')[0].scrollHeight);

function test_send(){
    var q = $('#question').val();
    if (q){
    let d = `
    <div class="row mt-3 me-3">
    <div class="col-12">
    <div class="btn btn-light btn-lg rounded-5 col-3 col-xl-2 text-start disabled" style="float:right;">
    <h5 class="text-dark">${q}</h5>
    </div>
    </div>
    </div>`;
    $('#question').empty();
    $('#communication').append(d);
    var postdata ={
            "question" : q
            }
    document.getElementById("question").value ='';
    $.ajax({
        type:'POST',
        url:'http://localhost:80/test/'+subject,
                    async : true,
        data: JSON.stringify(postdata),
        dataType : 'JSON',
        contentType: "application/json",
        success: function(airesponse){
            let r = airesponse.result2['data'];
            let r2 = airesponse.result2['answer_audio'];

            let audio_response2  = `<div class="row mt-5 ms-4">
            <div class="col-12" >
            <audio controls src= "data:audio/mp3;base64,${r2}" ></audio>
            </div>
            </div>
            </div>`; // `이거로
            $('#communication').append(audio_response2);

            let str_response = `<div class="row mt-3 ms-4">
            <div class="col-12">
            <div class="btn btn-light btn-lg rounded-5 col-3 col-xl-2 text-start disabled">
            <h5 class="text-dark"> ${r}</h5>
            </div>
            </div>
            </div>`; // `이거로
        $('#communication').append(str_response);
        $('#communication').scrollTop($('#communication')[0].scrollHeight);
        },
    })

    $('#communication').scrollTop($('#communication')[0].scrollHeight);
}
}

function audio_send(){
    document.getElementById('audioe').style.display='none';
    document.getElementById('text-send').style.display='block';
    document.getElementById('audio_send').style.display='none';
    document.getElementById('trash-recording').style.display='none';
    document.getElementById('start-recording').style.display='block';

    var formData = new FormData();
    file = new File([recorder.getBlob()], "audio.wav",);
    formData.append("audio",file);

    let audio_response = `<div class="row mt-3 me-3">
            <div class="col-12" >
            <audio controls src= "${audio.src}" style="float:right;" ></audio>
            </div>
            </div>
            </div>`; // `이거로
    $('#communication').append(audio_response);

    recorder = null;

    $.ajax({
        type:'POST',
        url:'http://localhost:80/test/audio/'+subject,
        processData:false,
        contentType:false,
        data: formData,
    success: function(airesponse){
        let r1 = airesponse.result2['request'];
        let r2 = airesponse.result2['data'];
        let r3 = airesponse.result2['answer_audio'];

        let a_text = `
        <div class="row mt-3 me-3">
        <div class="col-12">
        <div class="btn btn-light btn-lg rounded-5 col-3 col-xl-2 text-start disabled" style="float:right;">
        <h5 class="text-dark">${r1}</h5>
        </div>
        </div>
        </div>`;
        $('#communication').append(a_text);

        let audio_response2  = `<div class="row mt-5 ms-4">
            <div class="col-12" >
            <audio controls src= "data:audio/mp3;base64,${r3}" ></audio>
            </div>
            </div>
            </div>`; // `이거로
        $('#communication').append(audio_response2);

        let str_response = `<div class="row mt-3 ms-4">
            <div class="col-12">
            <div class="btn btn-light btn-lg rounded-5 col-3 col-xl-2 text-start disabled">
            <h5 class="text-dark"> ${r2}</h5>
            </div>
            </div>
            </div>`; // `이거로
        $('#communication').append(str_response);
        $('#communication').scrollTop($('#communication')[0].scrollHeight);
        },
    })




}