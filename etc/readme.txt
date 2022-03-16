
꿀팁 정리

1. 테일윈드

테일윈드 설치하면 package.json / package-lock.json / tailwind.config.js 나옴.
설치방법은
npm install -D tailwindcss
npx tailwindcss init

경로설정
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

css에 등록
@tailwind base;
@tailwind components;
@tailwind utilities;

project.json에서 css에 등록함으로써
npx tailwindcss -i ./base/static/common.base.css -o ./base/static/common.css --watch
이것을 npm run css로 실행 가능

아래 터미널에서 로컬 두개 열어서, 하나는 npm run css, 하나는 python manage.py runserver 해줄 것
실시간 테일윈드 변경 가능


requirement 한번에 설치
pip install -r requirements/dev.txt










if(one){
const arr = [one, two, three, four, five]

arr.forEach(item=> item.addEventListener('mouseover', (event)=> {handleSelect(event.target.id)}))

arr.forEach(item=> item.addEventListener('click', (event)=>{
    const val = event.target.id
    console.log(val)
    let numval = getNumericValue(val)
        console.log(numval)


//    starForm.addEventListener('submit', e=>{
//            e.preventDefault()
//            if (isSubmit){
//                return
//            }
//            isSubmit=true
//
//            const id = e.target.id
//            console.log(id)
//            const val_num = getNumericValue(val)
//
//
////            $.ajax({
////                type:'POST',
////                url:'rate/'
////                data:{
////                    'csrfmiddlewaretoken': csrf[0].value
////                    'el_id' = id
////                    'val' = val_num
////                },success: function(response){
////                    console.log(response)
////                    confirmBox.innerHTML=`<hi>점수 등록이 완료되었음..${response.score}</h1>`
////                },
////                error: function(error){
////                    console.log(error)
////                    confirmBox.innerHTML = '<h1>Ups... something went wrong</h1>'
////                }
////            })
//        })
    }))
}

필요사항(ERD 제작)
필로우
마이에스큐엘클라이언트
장고익스텐션

#https://dreampuf.github.io/GraphvisOnline
./manage.py graph_models -a >my_project.dot
./manage.py graph_models -a > graph_models.dot
./manage.py graph_models -a > graph_models.dot
