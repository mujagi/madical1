$(function(){
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [76,91,81,99,61,82,63,80,64,55];
    let eng = [60,75,58,56,96,85,59,58,98,65];
    let math = [73,88,56,61,77,69,76,65,68,81];
    let total = [209,254,195,216,234,236,198,203,230,201];
    let avg = [69.6,84.6,65,72.6,78,78.7,66,67,76.6,67];

    let htmlData = "";
    for(let i=0;i<no.length;i++){
        htmlData+="<tr id="+no[i]+">";
        htmlData+="<td><input type='checkbox' name='stu' class='stuChk' value="+no[i]+"></td>";
        htmlData+="<td>"+no[i]+"</td>";
        htmlData+="<td>"+name[i]+"</td>";
        htmlData+="<td>"+kor[i]+"</td>";
        htmlData+="<td>"+eng[i]+"</td>";
        htmlData+="<td>"+math[i]+"</td>";
        htmlData+="<td>"+total[i]+"</td>";
        htmlData+="<td>"+avg[i]+"</td>";
        htmlData+="<td>0</td>";
        htmlData+="</tr>";
    }
    $("#body").html(htmlData);

    $("#confirmBtn").click(function(){
        if($("#name").val().length<2){
            alert("이름을 입력하셔야 합니다!");
            $("#name").focus();
            return false;
        }
        else if($("#kor").val().length<1){
            alert("국어 점수를 입력하셔야 합니다!");
            $("#kor").focus();
            return false;
        }
        else if($("#eng").val().length<1){
            alert("영어 점수를 입력하셔야 합니다!");
            $("#eng").focus();
            return false;
        }
        else if($("#math").val().length<1){
            alert("수학 점수를 입력하셔야 합니다!");
            $("#math").focus();
            return false;
        }
        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no);
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = i_total/3 ;
        let htmlData = "";
        htmlData += "<tr id='"+i_no+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
        htmlData += "<td>"+i_no+"</td>";
        htmlData += "<td>"+i_name+"</td>";
        htmlData += "<td>"+i_kor+"</td>";
        htmlData += "<td>"+i_eng+"</td>";
        htmlData += "<td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td>";
        htmlData += "<td>"+i_avg+"</td>";
        htmlData += "<td>0</t3d>";
        htmlData += "</tr>";
        $("#body").append(htmlData);
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");
    })
    



    $("#deleteBtn").click(function(){
        console.log("체크박스 개수 : "+ $(".stuChk").length);
        console.log("체크박스에서 체크된 개수  : "+ $(".stuChk:checked").length);
        console.log("체크박스에서 체크된 개수  : "+ $("input:checkbox[name='stu']:checked").length);
        if($(".stuChk:checked").length<1){
            alert("삭제할 항목을 선택하세요!!!");
            return false;
        };
        if(!confirm("정말 삭제하시겠습니까?")){
            return false;
        };
        $(".stuChk").each(function(){
            if($(this).is(":checked")==true){
                console.log("class 값 : "+$(this).val());
                console.log("id 값 : "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            };
        })
    })  


    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
    })
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none ");
    })

    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            })
        };
    })
    
    $("#modifyBtn").click(function(){
        $(".result").css("display","block");
    })
    $("#stu_search").click(function(){
        $(".result").css("display","none");
    })
    $("#stu_search").click(function(){
        
    })
})