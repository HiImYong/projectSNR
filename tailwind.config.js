module.exports = {
  mode: "jit", // jit 모드 실행
  prefix: "t-", //부트스트랩과 테일윈드 충돌 회피
  content: ["./templates/*.{html,js}"], // 이 프로젝트의 html이나 js로 끝나는 것들을 체크하겠다.
  theme: {
    extend: {},
  },
  plugins: [],
}

