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
//////////////////////////////////////////////////////////////////////////

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


if (one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id)
    }))

    arr.forEach(item=> item.addEventListener('click', (event)=>{
        // value of the rating not numeric
        const val = event.target.id

        let isSubmit = false
        form.addEventListener('submit', e=>{
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true
            // picture id
//            const id = e.target.id
            // value of the rating translated into numeric
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
                    confirmBox.innerHTML = `<h1>이 라켓의 별점은 <span class="t-text-red-500 t-text-xl">${val_num}</span>점이에요!</h1>`
                    document.getElementById(`inputNumForm`).value = `${val_num}`
                    console.log(val)
                    console.log(val_num)

                },
                error: function(error){
                    console.log(error)
                    confirmBox.innerHTML = '<h1>Ups... something went wrong</h1>'
                }
            })
        })
    }))
}

