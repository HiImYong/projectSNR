console.log("hello~~~~~");

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form') // form에 들어간 rate-form 클래스
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

//////////////////////////////////////////////////////////////////////////////////

const handleStarSelect = (size) => {  //가장 아래에서 행렬별 별 색상바꿀 때 적용되는 메소드
    const children = form.children
    for (let i=0; i < children.length; i++)
    if(i<= size){
    children[i].classList.add('checked')
    } else{
    children[i].classList.remove('checked')
    }

}

const handleSelect = (selection) => {
    switch(selection){
        case 'first':{
        handleStarSelect(1)
        return
        }
                case 'second':{
        handleStarSelect(2)
        return
        }
                case 'third':{
        handleStarSelect(3)
        return
        }
                case 'fourth':{
        handleStarSelect(4)
        return
        }
                case 'fifth':{
        handleStarSelect(5)
        return
        }
    }
}
////////////////////////////////////////////////////////////////////////// 선택한 것에 따른 점수

const getNumericValue = (stringValue) => {
    let numericValue;
    if(stringValue === 'first'){
        numericValue = 1
    }
    else if(stringValue === 'second'){
        numericValue = 2
    }
    else if(stringValue === 'third'){
        numericValue = 3
    }
    else if(stringValue === 'fourth'){
        numericValue = 4
    }
    else if(stringValue === 'fifth'){
        numericValue = 5
    }
    else{
        numericValue = 0
    }

    return numericValue

}
////////////////////////////////////////////////////////////////////////// 각 버튼별 행렬 구현, 마우스 오버, 클릭 구현


if (one) {  //1. 만약 one 변수가 있다면
    const arr = [one, two, three, four, five] // 2. 행렬을 만들어준다.

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{ //3. 마우스 오버에 대한 별 색상 변경 이벤트
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{ //4. 별을 클릭했을 때 발생하는 이벤트
        const val = event.target.id

        let isSubmit = false // 5. isSubmit 변수 선언. 현재 별점이 제출 되었는지 여부 판단
        form.addEventListener('submit', e=>{ // 6. 제출이 실행되면 이하 내용 실행 시작
        ////////////-------------------------------------------------------------------------------------------------//////////////
            e.preventDefault() // a 태그나 submit 태그는 누르게 되면 href 를 통해 이동하거나 , 창이 새로고침하여 실행되는데 이것을 못하게 막음
            if (isSubmit) { // 7. 만약 isSubmit 이 True라면
                return  // 8.폼 값을 제출한다.
            }
            isSubmit = true // 9. isSubmit을 True로 바꿔준다
            const val_num = getNumericValue(val)  //10. val_num 변수 선언.
            $.ajax({
                type: 'POST',
                url: '/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
//                    'el_id': id,
                    'val': val_num,
                },
                success: function(response){
                    console.log(response)
                    confirmBox.innerHTML = `<h1>이 라켓의 별점을 <span class="t-text-red-500 t-text-xl">${val_num}</span>점으로 제출합니다</h1>`
                    document.getElementById(`inputNumForm`).value = `${val_num}` // 이 부분에서 폼에 값이 들어감.
                    console.log(val)
                    console.log(val_num)

                },
                error: function(error){
                    console.log(error)
                    confirmBox.innerHTML = '<h1>내용에 문제가 있습니다. 관리자에게 문의하세요.</h1>'
                }
            })
        })
    }))
}

