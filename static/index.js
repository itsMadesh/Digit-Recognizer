let pre=null
const view = () =>{
    const htm=`<div class="wrapper">
        <img src="static/images/digit.png" alt="digit" >
        <div class="value">Recognized value is ${pre}</div>
    </div>`;
    $(".result").append(htm);
}
handleGetValue = ()=>{
    const index=$("#index").val();
    console.log(index);
    $.ajax({
        method:"GET",
        url:"/digit",
        data:{"index":index},
        dataType:"text",
        contentType:"application/json",
        success: async function(res){
            pre=JSON.parse(res);
            pre=pre["predictedValue"];
            await view();
        }
    });

}
