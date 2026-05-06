# 04week CSS Transform / Transition / Animation

## 1. 예제 파일별 CSS 속성 설명

### transform.html

`transform.html`은 요소의 모양과 위치를 바꾸는 `transform` 속성을 다룹니다.

- `transform: translate(x, y);`
  - 요소를 현재 위치 기준으로 x축, y축만큼 이동시킵니다.
  - 예제에서는 `.translate:hover`에 `translate(100px, 100px)`를 적용하여 마우스를 올리면 오른쪽으로 100px, 아래로 100px 이동합니다.

- `transform: scale(x, y);`
  - 요소의 크기를 x축, y축 방향으로 확대하거나 축소합니다.
  - 예제에서는 `.scale:hover`에 `scale(2, 2)`를 적용하여 요소가 가로, 세로 2배로 커집니다.

- `transform: rotate(angle);`
  - 요소를 지정한 각도만큼 회전시킵니다.
  - 예제에서는 `.rotate:hover`에 `rotate(90deg)`를 적용하여 요소가 90도 회전합니다.

- `transform: skew(x-angle, y-angle);`
  - 요소를 x축, y축 방향으로 기울입니다.
  - 예제에서는 `.skew:hover`에 `skew(30deg, 30deg)`를 적용하여 요소가 양쪽 방향으로 기울어집니다.

- `:hover`
  - 마우스를 요소 위에 올렸을 때 적용되는 선택자입니다.
  - 이 예제에서는 마우스를 올렸을 때만 `transform` 효과가 나타납니다.

### transition.html

`transition.html`은 CSS 속성 값이 바뀔 때 변화 과정을 부드럽게 보여주는 `transition` 속성을 다룹니다.

- `transition: 시간;`
  - CSS 속성 변화가 지정한 시간 동안 서서히 일어나도록 만듭니다.
  - 예제에서는 `transition: 2s`, `transition: 4s`, `transition: 0.5s`처럼 요소마다 다른 변화 시간을 적용했습니다.

- `background-color`, `background`
  - 요소의 배경색을 지정합니다.
  - 예제에서는 `:hover` 상태에서 배경색이 바뀌고, `transition` 때문에 색 변화가 부드럽게 보입니다.

- `color`
  - 글자 색을 지정합니다.
  - 예제에서는 `.translate:hover`에서 글자 색이 흰색으로 바뀝니다.

- `transform`과 `transition` 함께 사용하기
  - `transform`만 사용하면 변화가 즉시 일어납니다.
  - `transition`을 함께 사용하면 이동, 확대, 회전, 기울임 효과가 부드럽게 진행됩니다.

### animation.html

`animation.html`은 `@keyframes`와 `animation` 관련 속성을 사용해 자동으로 반복되는 움직임을 만드는 예제입니다.

- `@keyframes`
  - 애니메이션의 시작, 중간, 끝 상태를 정의합니다.
  - `0%`, `50%`, `100%` 또는 `from`, `to`를 사용해 각 시점의 CSS 상태를 지정할 수 있습니다.

- `animation-name`
  - 실행할 `@keyframes` 이름을 지정합니다.
  - 예제에서는 `.box1`에 `animation-name: move;`를 적용했습니다.

- `animation-duration`
  - 애니메이션이 한 번 실행되는 데 걸리는 시간을 지정합니다.
  - 예제에서는 `.box1`이 `2s` 동안 움직입니다.

- `animation-direction: alternate;`
  - 애니메이션을 정방향과 역방향으로 번갈아 실행합니다.
  - 예제에서는 요소가 오른쪽으로 갔다가 다시 왼쪽으로 돌아오는 것처럼 보입니다.

- `animation-iteration-count: infinite;`
  - 애니메이션 반복 횟수를 지정합니다.
  - `infinite`는 무한 반복을 의미합니다.

- `animation`
  - 여러 애니메이션 속성을 한 줄로 작성하는 단축 속성입니다.
  - 예제의 `animation: animation 3s alternate infinite;`는 이름, 시간, 방향, 반복 여부를 한 번에 지정합니다.

- `animation-timing-function`
  - 애니메이션 속도 변화를 지정합니다.
  - 예제의 `.ball`은 `ease-in`을 사용해 점점 빨라지는 느낌을 줍니다.

- `border-radius`
  - 요소의 모서리를 둥글게 만듭니다.
  - 예제에서는 사각형을 원처럼 보이게 하거나, 공이 바닥에 닿을 때 찌그러지는 효과를 만드는 데 사용했습니다.

## 2. 숙제: card.html 예제 완성하기

`card.html` 예제를 완성해오세요.

튜티들에게는 `card.html` 파일만 제공됩니다. CSS에 작성된 class 이름과 구조를 보고, 그에 맞는 HTML 구조를 직접 만들어야 합니다.

완성된 예제는 다음 동작을 포함해야 합니다.

- 카드 제목이 화면에 표시되어야 합니다.
- 카드 앞면과 뒷면이 존재해야 합니다.
- 마우스를 카드 위에 올리면 카드가 Y축으로 회전하며 뒤집혀야 합니다.
- 카드가 좌우로 움직이는 애니메이션이 적용되어야 합니다.
- 카드 앞면에는 칩 영역과 은행 이름이 보여야 합니다.
- 카드 뒷면에는 검은 줄, 이름, 카드 번호 정보가 보여야 합니다.

## 3. 힌트

- 카드 전체를 감싸는 바깥 요소에는 3D 회전을 자연스럽게 보이게 하기 위해 `perspective`를 사용할 수 있습니다.
  - 예: `.cardBox`

- 실제로 뒤집히는 카드 요소에는 회전 애니메이션이 부드럽게 보이도록 `transition`을 적용합니다.
  - 예: `.card`

- 카드의 앞면과 뒷면이 3D 공간에서 따로 존재하도록, 회전하는 카드 요소에 `transform-style: preserve-3d`를 사용합니다.
  - 이 속성이 없으면 앞면과 뒷면이 납작하게 겹쳐 보여 의도한 카드 뒤집기 효과가 잘 나오지 않습니다.

- 카드 앞면과 뒷면에는 같은 위치에 겹쳐지도록 `position: absolute`를 사용할 수 있습니다.
  - 예: `.card > div`

- 카드가 뒤집혔을 때 반대쪽 면이 비쳐 보이지 않게 하려면 앞면과 뒷면에 `backface-visibility: hidden`을 적용합니다.
  - 예: `.card-front`, `.card-back`

- 카드 뒷면은 처음부터 뒤집힌 상태로 배치해야 하므로 `transform: rotateY(180deg)`를 사용합니다.
  - 예: `.card-back`

- 마우스를 올렸을 때 카드가 뒤집히게 하려면 hover 선택자에서 실제 카드 요소를 `rotateY(180deg)`만큼 회전시킵니다.
  - 예: `.cardBox:hover .card`

- 카드가 좌우로 움직이게 하려면 `@keyframes`에서 `left` 값을 바꾸고, 카드 바깥 요소에 `animation`을 적용합니다.
  - 예: `.cardBox`, `@keyframes card`

- 카드 안의 칩, 은행 이름, 뒷면의 선과 정보 영역은 `position: relative`, `top`, `left`, `right`, `width`, `height` 등을 조절해서 원하는 위치에 배치합니다.
  - 예: `.ic`, `.bank`, `.line`, `.info`
