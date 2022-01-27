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

const handleStarSelect = (size) => {
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


if (one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        const val = event.target.id

        let isSubmit = false
        form.addEventListener('submit', e=>{
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true

            const val_num = getNumericValue(val)

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
                    document.getElementById(`inputNumForm`).value = `${val_num}`
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

