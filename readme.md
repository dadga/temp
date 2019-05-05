## selenium 설치

* 구글 크롬에서 selenium extension을 설치한다. https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?hl=en

## 조사 대상 리스트
전국 330개 대학
https://docs.google.com/spreadsheets/d/1d53I0kMRDD-2b5OBtcxr3dPz5huc-OPv8ZdhkkzLj5c/edit?usp=sharing

* 상태를 "작업중"으로 변경하고 작업 시작, 작업이 완료되고 나면 "완료"로 변경, "미처리"의 경우 "비고" 칼럼에 이유를 기입.
* 작업자는 추후 변경될 수 있음.
* side 파일 작업이 완료되는 대로 수시로 github에 올린다.
* 남들이 작업한 side 파일에 대해 상호검증을 한다. 본인이 작업한 것은 "본인"이라고 적는다. 상호검증의 완료되면 "O", 검증이 미진하면 그 원인을 기입.
* 작업을 하거나 상호검증을 하다가 의문나는 사항이 있으면 Trello - Issue에 Card를 추가해서 그 내용을 적는다.

## side 파일 만드는 방법

* chrome에서 selenium extension 버튼을 클릭한다.
* Record a new test in new project를 선택한다.
* PROJECT NAME에는 대학교명을 입력한다(예 : KC대학교)
* BASE URL에는 사이트 주소를 입력한다. 가급적이면 "www"를 붙이지 않는다(예 : http://kcu.ac.kr).
  * URL에 "https://" 를 붙이지 않고 "http://" 를 붙인다.
  * 도메인 마지막에는 슬래시를 붙이지 않는다.
* Start Recording을 누른다.
* 사이트 메인 페이지에서 "로그인", "포털", "웹메일", "인트라넷" 등을 찾아 클릭한다.
* ID에는 "testtest"를 입력한다. 간혹 메일 형식으로 입력을 해야 하는 경우에는 "test@test.net"을 입력한다.
* PW에는 "11111111"을 입력한다.
* 로그인 버튼을 누른다(당연히 로그인은 안됨).
* 화면을 닫는다. (열려있는 창은 되도록 다 닫는다.)
* selenium에서 Stop Recording을 누른다.
* 파일을 저장한다(예 : kcu.ac.kr.side)
* "setWindowSize" 부분을 지운다.
* https://github.com/dadga/temp/side에 올린다.

### side 파일 만들때 고려사항
* 하나의 사이트에 여러개의 로그인 페이지가 있을경우 여러개의 tests를 추가하여 구분한다.
  * Selenium IDE 왼쪽 상단에 "add new test"를 통해 test를 추가한다.
* Test PC에서 Allou Popup 미리 준비하고 ActiveX도 미리 설치해서 테스트할 예정
  * 사이트에서 팝업요청이 있을 경우 팝업을 허용한다.
  * 사이트에서 ActiveX 또는 추가 보안프로그램 설치를 요구할 경우 설치한다.
