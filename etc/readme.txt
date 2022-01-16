
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



