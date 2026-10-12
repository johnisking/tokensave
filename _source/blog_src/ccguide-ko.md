![클로드 코드 사용법: 설치부터 첫 작업까지 실제 화면으로](/claude-code-sayongbeop-ko.jpg)

클로드 코드 사용법을 찾아보면 첫 단계에서 막혔다는 이야기가 의외로 많습니다. 설치 명령어는 한 줄인데 윈도우에서는 PowerShell과 CMD에서 쓰는 명령어가 다르고, 설치 방법에 따라서는 실행하자마자 빨간 오류가 뜨기도 합니다. 이 글에서는 윈도우 PowerShell에서 설치 확인, 테마 선택, 첫 작업 지시, 사용량 확인까지 직접 진행한 화면을 보면서 공식 문서를 기준으로 클로드 코드 설치 방법과 기본 사용법을 순서대로 정리합니다. 중간에 실제로 만난 오류와 해결 방법도 그대로 담았습니다.

## 클로드 코드란?

클로드 코드(Claude Code)는 Anthropic이 만든 AI 코딩 에이전트입니다. 터미널(PowerShell이나 macOS 터미널)에서 `claude`를 입력하면 대화 화면이 열리고, 한국어로 "이 파일 고쳐 줘", "테스트 코드 짜 줘"라고 부탁하면 클로드가 프로젝트 파일을 읽고, 코드를 고치고, 명령어를 실행하는 데까지 알아서 진행합니다. 채팅창에 코드를 붙여 넣고 주고받는 방식이 아니라 **내 컴퓨터 폴더 안에서 직접 작업한다**는 점이 가장 큰 차이입니다.

공식 문서에 따르면 클로드 코드는 터미널 말고도 웹(claude.ai/code), 데스크톱 앱, VS Code·JetBrains 확장 프로그램, Slack, GitHub Actions 등에서도 쓸 수 있습니다. 이 글은 가장 기본이 되는 터미널판(CLI) 사용법을 다룹니다. 터미널이 낯설다면 데스크톱 앱에서 쓰는 방법도 있습니다.

## 시작하기 전에 필요한 것

### 지원 운영체제와 컴퓨터 사양

공식 문서 'Advanced setup'에 나온 실행 조건은 다음과 같습니다(2026년 10월 12일 확인).

| 항목 | 조건 |
|---|---|
| 운영체제 | macOS 13.0 이상, Windows 10 1809 이상 또는 Windows Server 2019 이상, Ubuntu 20.04 이상, Debian 10 이상, Alpine Linux 3.19 이상 |
| 하드웨어 | 메모리 4GB 이상, x64 또는 ARM64 프로세서 |
| 네트워크 | 인터넷 연결 필요 |
| 셸 | Bash, Zsh, PowerShell, CMD |
| 지역 | Anthropic 서비스 지원 국가(한국 포함) |

윈도우에서는 관리자 권한으로 실행할 필요가 없습니다. Git for Windows는 필수가 아니지만, 설치해 두면 클로드 코드가 Git Bash로 명령어를 실행합니다. 없으면 PowerShell을 대신 씁니다.

### 유료 요금제 또는 콘솔 계정

여기서 많이 놓치는 부분이 있습니다. **클로드 코드는 클로드 무료 요금제로는 쓸 수 없습니다.** 공식 문서에는 Pro, Max, Team, Enterprise 또는 Claude Console(API) 계정이 필요하다고 적혀 있습니다.

| 계정 | 클로드 코드 | 결제 방식 |
|---|:---:|---|
| Free(무료) | × | – |
| Pro | ○ | 월 $20(연간 결제 시 월 $17) |
| Max 5x / Max 20x | ○ | 월 $100 / $200 |
| Team·Enterprise | ○ | 좌석(사용자)별 계약 |
| Claude Console(API) | ○ | 쓴 토큰만큼 종량제 |

구독 요금제에서는 클로드 코드와 클로드 앱(웹·데스크톱·모바일)이 **같은 사용량 한도를 함께 씁니다.** 요금제별 가격과 한도 비교는 [클로드 요금제 총정리](/ko/blog/claude-yogeumje)와 [클로드 코드 요금 한 달에 얼마?](/ko/blog/claude-code-yogeum)에 정리해 두었습니다.

## 클로드 코드 설치 방법

### 공식 추천은 네이티브 설치

공식 문서가 '추천'으로 표시한 방법은 네이티브 설치 프로그램입니다. 내 환경에 맞는 한 줄을 터미널에 붙여 넣고 실행하면 됩니다.

**macOS·Linux·WSL**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD**

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

PowerShell인지 CMD인지는 프롬프트 맨 앞을 보면 알 수 있습니다. `PS C:\Users\사용자이름>`처럼 **앞에 PS가 붙어 있으면 PowerShell**, 없으면 CMD입니다. 공식 문서에 따르면 다음 오류가 뜨면 명령어를 바꿔 넣은 것입니다.

- `The token '&&' is not a valid statement separator` → PowerShell에서 CMD용 명령어를 실행함
- `'irm' is not recognized as an internal or external command` → CMD에서 PowerShell용 명령어를 실행함

설치하는 동안에는 진행 표시가 나오지 않으니 끝날 때까지 잠시 기다리면 됩니다.

### 다른 설치 방법

| 방법 | 명령어 | 자동 업데이트 |
|---|---|:---:|
| 네이티브(추천) | 위 3가지 | ○(백그라운드 자동) |
| Homebrew(macOS) | `brew install --cask claude-code` | ×(`brew upgrade` 필요) |
| WinGet(Windows) | `winget install Anthropic.ClaudeCode` | ×(`winget upgrade` 필요) |
| npm | `npm install -g @anthropic-ai/claude-code` | 조건부 |

npm으로 설치하려면 Node.js 22 이상이 필요합니다. 설치되는 프로그램은 네이티브 설치와 같지만, `sudo npm install -g`는 권한 문제를 일으키니 쓰지 말라고 공식 문서에 경고가 있습니다. npm판은 윈도우에서 다음에 설명할 오류가 나기 쉬우니, 새로 설치한다면 네이티브 설치 프로그램을 고르는 편이 무난합니다.

## 설치 확인하기 (윈도우에서 난 오류와 해결법)

설치가 끝나면 **새 터미널 창을 열고** 다음 명령어로 버전을 확인합니다.

```powershell
claude --version
```

제대로 설치됐다면 버전 번호 뒤에 `(Claude Code)`가 표시됩니다.

### "running scripts is disabled" 오류가 뜰 때

실제로 윈도우 PowerShell에서 `claude --version`을 실행했더니 버전 대신 빨간 오류가 떴습니다.

![PowerShell에서 claude --version 실행 시 뜬 실행 정책 오류 화면](/claude-code-sayongbeop-ps1-error-ko.jpg)

오류 문구에 `npm\claude.ps1 cannot be loaded because running scripts is disabled on this system`이라고 나옵니다. 이 컴퓨터에는 클로드 코드가 npm으로 설치되어 있었습니다. 공식 문제 해결 문서에 따르면, npm은 명령어마다 `.ps1` 스크립트 파일을 실행용으로 만드는데 PowerShell의 **실행 정책**이 이 스크립트를 막아서 생기는 오류입니다. PowerShell 설치 명령어(`irm ... | iex`)는 스크립트 파일을 쓰지 않아서 이 영향을 받지 않습니다.

공식 문서가 안내하는 해결 방법은 세 가지입니다.

1. **내 사용자 계정에서만 로컬 스크립트를 허용하기**

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **`.cmd` 실행 파일 쓰기**. `claude.cmd`는 같은 역할을 하고 실행 정책의 영향을 받지 않습니다.
3. **npm 대신 PowerShell 설치 프로그램으로 다시 설치하기**. 스크립트가 아니라 실행 파일이 설치됩니다.

이번에는 설정을 바꾸지 않아도 되는 두 번째 방법으로 확인했습니다. `claude.cmd --version`을 입력하자 버전이 나왔습니다.

![claude.cmd --version으로 2.1.295 (Claude Code)가 표시된 화면](/claude-code-sayongbeop-version-ko.jpg)

표시된 버전은 `2.1.295 (Claude Code)`였습니다. 설치 상태를 더 자세히 보고 싶다면 `claude doctor`를 실행하면 설치 상태, 설정 파일 오류, 해결 방법 제안 등이 나옵니다.

### "claude를 찾을 수 없음"이 뜰 때

`command not found: claude`나 `'claude' is not recognized`가 뜨는 건 설치 폴더가 아직 PATH에 등록되지 않았기 때문입니다. 먼저 터미널을 닫았다가 다시 열어 보고, 그래도 안 되면 공식 문서 'Troubleshoot installation and login'의 'Fix your PATH' 안내를 따릅니다.

## 첫 세션 시작하기

### 작업용 폴더를 만들고 이동하기

클로드 코드는 **실행한 폴더**를 작업 공간으로 삼습니다. 사용자 폴더 전체에서 바로 실행하기보다 연습용 폴더를 하나 만들고 그 안에서 실행하는 편이 안심됩니다.

```powershell
mkdir claude-test
cd claude-test
```

![PowerShell에서 mkdir와 cd로 claude-test 폴더를 만들고 이동한 화면](/claude-code-sayongbeop-mkdir-ko.jpg)

실제 개발할 때는 작업할 프로젝트 폴더로 `cd`해서 들어간 뒤 실행하면 됩니다.

### claude로 실행하고 테마 고르기

폴더 안에서 `claude`(npm판에서 실행 정책 오류가 나면 `claude.cmd`)를 입력하면 클로드 코드가 실행됩니다. 처음에는 글자 색 구성(테마)을 고르는 화면이 나옵니다.

![클로드 코드 첫 실행 때 나오는 테마 선택 화면](/claude-code-sayongbeop-theme-ko.jpg)

선택지는 Auto(터미널에 맞춤), Dark mode, Light mode와 각각의 색약 친화 버전, ANSI 색상 전용 버전입니다. 화면 아래에 코드 변경 표시 예시가 나오니 보기 편한 것을 화살표 키로 고르고 Enter를 누르면 됩니다. 나중에 `/theme`으로 바꿀 수 있습니다.

### 로그인하기

다음은 로그인입니다. 공식 문서에 따르면 첫 실행 때 브라우저가 열리고, 안내에 따라 클로드 계정으로 인증하는 흐름입니다. 한 번 로그인하면 인증 정보가 저장되어 다음부터는 다시 할 필요가 없습니다. 계정을 바꾸고 싶을 때는 실행 중인 화면에서 `/login`을 입력합니다.

이번 컴퓨터는 이미 클로드 데스크톱 앱을 쓰고 있던 상태였고, 로그인은 그냥 바로 됐습니다.

### 시작 화면 보는 법

로그인이 끝나면 다음과 같은 화면이 나옵니다.

![클로드 코드 시작 화면. 버전, 모델, 작업 폴더, auto mode 표시](/claude-code-sayongbeop-start-ko.jpg)

왼쪽 위에 클로드 코드 버전(v2.1.295), 사용 중인 모델과 요금제(Opus 5.5 · Claude Max), 작업 폴더(~\claude-test)가 표시됩니다. 맨 아래 `❯` 줄이 입력창입니다.

그 위의 노란 줄은 사용 중인 MCP 서버(외부 도구 연결)의 인증이 필요하다는 안내로, `/mcp`에서 설정할 수 있습니다. MCP를 쓰지 않으면 나오지 않습니다.

화면 맨 아래의 **auto mode on**은 권한 모드 표시입니다. 이 부분은 뒤에서 설명합니다.

## 첫 작업 시켜 보기

입력창에 원하는 일을 한국어로 그대로 쓰고 Enter를 누르면 됩니다. 이번에는 연습으로 파일 하나를 만들어 달라고 했습니다.

![클로드 코드에 hallo.txt를 만들어 달라고 하자 3초 만에 작성이 끝난 화면](/claude-code-sayongbeop-hello-ko.jpg)

처음에는 아무것도 입력하지 않은 채 Enter를 눌러서, 클로드가 "메시지가 비어 있다, 무엇을 할지" 묻고 지금 폴더가 Git 저장소가 아니라는 것도 알려 줬습니다. 이어서 "hallo.txt 파일을 만들고 안에 안녕하세요 라고써줘"라고 입력하자 `Write(hallo.txt)`가 표시되며 파일이 만들어졌고, 작업 시간은 "Brewed for 3s", 즉 약 3초였습니다.

클로드는 지시에 쓴 이름 그대로 파일을 만들고, 완료 보고도 "파일을 만들고 '안녕하세요'라고 썼습니다"라고 한국어로 답했습니다. 파일 이름이나 위치는 쓴 그대로 반영되니 정확하게 적는 것이 중요합니다.

### 익숙해지면 해 볼 만한 요청

공식 빠른 시작 문서는 실제 프로젝트에서 다음과 같은 요청을 해 보라고 권합니다(한국어로 옮김).

- "이 프로젝트는 뭘 하는 거야?", "폴더 구조 설명해 줘"
- "메인 파일에 hello world 함수 추가해 줘"
- "내가 바꾼 파일 알려 줘", "알아보기 쉬운 메시지로 커밋해 줘"
- "빈 양식이 제출되는 버그 고쳐 줘"
- "계산기 함수 단위 테스트 짜 줘"

공식 문서의 요령은 **구체적으로 부탁하기**입니다. "버그 고쳐 줘"보다 "비밀번호를 틀리면 화면이 하얗게 나오는 로그인 버그 고쳐 줘"가 원하는 결과에 더 가깝게 나옵니다. 큰 작업은 "1. 테이블 만들기 2. API 만들기 3. 화면 만들기"처럼 단계로 나눠 부탁하는 것도 효과적입니다.

## 권한 모드와 auto mode

![권한 모드와 auto mode: 모드, 확인 없이 실행되는 것, 이럴 때 좋음](/claude-code-sayongbeop-auto-mode-ko.jpg)

클로드 코드가 파일을 마음대로 고치거나 명령어를 실행해도 되는지는 **권한 모드**가 정합니다. 시작 화면에도 나왔듯이, 공식 문서에 따르면 v2.1.283부터 터미널 대화 세션은 **auto mode**로 시작합니다. auto mode에서는 분류기가 작업 하나하나의 위험을 확인해서 위험이 낮다고 판단한 것은 바로 실행하고 나머지는 막습니다.

| 모드 | 확인 없이 실행되는 것 | 이럴 때 좋음 |
|---|---|---|
| default | 읽기만 | 모든 작업을 직접 확인하고 싶을 때 |
| acceptEdits | 읽기, 파일 편집, 일반적인 파일 명령어 | 바뀌는 내용을 보며 진행할 때 |
| plan | 읽기(auto mode가 가능하면 승인된 명령어도) | 고치기 전에 코드부터 살펴보게 할 때 |
| auto | 거의 전부(뒤에서 안전 확인) | 긴 작업, 확인 횟수를 줄이고 싶을 때 |
| dontAsk | 작업 폴더 안 읽기와 미리 허용한 도구만 | CI나 스크립트 |

모드는 **Shift+Tab**으로 바꿀 수 있습니다. 처음이라 불안하다면 Shift+Tab으로 default나 acceptEdits로 바꾼 뒤 쓰면 변경할 때마다 확인 창이 뜹니다. 연습용 폴더에서 동작에 익숙해진 다음 평소 프로젝트에 쓰는 것을 추천합니다.

## 꼭 알아 둘 기본 명령어

### 터미널에서 쓰는 명령어

| 명령어 | 하는 일 |
|---|---|
| `claude` | 대화 모드로 실행 |
| `claude "작업"` | 첫 지시와 함께 실행 |
| `claude -p "질문"` | 한 번만 답하고 종료 |
| `claude -c` | 이 폴더의 가장 최근 대화 이어 가기 |
| `claude -r` | 지난 대화 골라서 다시 열기 |
| `claude --version` | 버전 표시 |
| `claude doctor` | 설치·설정 진단 |
| `claude update` | 바로 업데이트 |

### 클로드 코드 안에서 쓰는 명령어

실행된 화면의 입력창에 `/`를 치면 쓸 수 있는 명령어 목록이 나옵니다. 자주 쓰는 것만 추렸습니다.

| 명령어 | 하는 일 |
|---|---|
| `/help` | 도움말과 명령어 목록 |
| `/init` | 프로젝트 설명서 `CLAUDE.md` 만들기 |
| `/clear` | 대화를 비우고 새로 시작 |
| `/compact` | 지금까지 대화를 요약해 컨텍스트 비우기 |
| `/context` | 컨텍스트 사용량 보기 |
| `/model` | 모델 바꾸기 |
| `/effort` | 생각하는 정도(effort) 바꾸기 |
| `/resume` | 지난 대화 다시 열기 |
| `/rewind` | 대화나 코드를 이전 상태로 되돌리기 |
| `/memory` | `CLAUDE.md` 편집 |
| `/usage` | 사용량과 한도 보기(`/cost`도 같음) |
| `/exit` | 종료(Ctrl+D 두 번도 가능) |

주의할 점은 **`/`로 시작하는 명령어는 클로드 코드 안에서 입력한다**는 것입니다. PowerShell 프롬프트(`PS C:\...>`)에 `/usage`를 치면 PowerShell 명령어로 처리되어 오류가 납니다. 실제로 처음에 이렇게 입력했다가 오류를 봤습니다.

### /init으로 CLAUDE.md 만들기

프로젝트에서 본격적으로 쓸 거라면 처음에 `/init`을 실행해 두면 편합니다. 클로드가 프로젝트를 살펴보고 구조와 빌드 방법 등을 정리한 `CLAUDE.md`를 만듭니다. 이 파일은 매번 대화를 시작할 때 읽히기 때문에 같은 설명을 반복하지 않아도 됩니다.

## 사용량 확인하기 (/usage)

구독 요금제로 쓴다면 신경 쓰이는 것이 사용량 한도입니다. 클로드 코드 안에서 `/usage`를 입력하면 설정 화면의 Usage 탭이 열립니다.

![클로드 코드 /usage 화면. 현재 세션 24%, 이번 주 45%, Fable 0%](/claude-code-sayongbeop-usage-ko.jpg)

이 화면에서 막대 3개를 확인할 수 있었습니다.

- **Current session(현재 세션)**: 24%. 5시간마다 초기화되는 한도입니다.
- **Current week (all models)(이번 주·전체 모델)**: 45%. 주 단위로 초기화되는 한도입니다.
- **Current week (Fable)(이번 주·Fable)**: 0%. Fable 모델 전용 주간 한도입니다.

이 숫자에는 클로드 코드뿐 아니라 같은 계정으로 쓴 클로드 앱 사용량도 들어갑니다. 아래쪽에는 사용량 구성 참고 정보와, 한도를 넘은 뒤에도 유료로 계속 쓸 수 있는 'Usage credits' 설정(`/usage-credits`)이 나옵니다. 한도가 어떻게 계산되는지와 아끼는 방법은 [클로드 코드 사용량 한도 정리](/ko/blog/claude-code-sayongnyang-hando)와 [클로드 코드 토큰 절약 방법](/ko/blog/claude-code-token-jeolyak)에 자세히 정리했습니다.

## 직접 써 보니

저는 무료에서 Pro로, 그리고 지금의 Max 5x로 옮겨 왔습니다. 평소에는 PC 한 대에서 클로드 데스크톱 앱으로 작업합니다. 코딩 작업과 외부 MCP 작업을 할 때는 토큰이 많이 들어서 Pro보다는 Max가 맞다고 느꼈고, 그 외 작업만 한다면 Pro로도 충분하다고 느꼈습니다.

## 업데이트와 삭제

네이티브로 설치했다면 클로드 코드는 실행할 때와 실행 중에 업데이트를 확인하고 백그라운드에서 자동으로 업데이트됩니다. 바로 최신으로 바꾸고 싶으면 `claude update`를 실행합니다. Homebrew나 WinGet으로 설치했다면 자동 업데이트가 되지 않으니 `brew upgrade claude-code`나 `winget upgrade Anthropic.ClaudeCode`를 주기적으로 실행합니다.

삭제는 설치한 방법에 맞춰 합니다.

| 설치 방법 | 삭제 방법 |
|---|---|
| 네이티브(macOS·Linux·WSL) | `~/.local/bin/claude`와 `~/.local/share/claude` 삭제 |
| 네이티브(Windows) | `%USERPROFILE%\.local\bin\claude.exe`와 `%USERPROFILE%\.local\share\claude` 삭제 |
| Homebrew | `brew uninstall --cask claude-code` |
| WinGet | `winget uninstall Anthropic.ClaudeCode` |
| npm | `npm uninstall -g @anthropic-ai/claude-code` |

설정과 대화 기록은 `~/.claude` 폴더와 `~/.claude.json`에 남습니다. 이것까지 지우면 설정, 허용한 도구, MCP 서버 설정, 세션 기록이 모두 사라지니 주의하세요.

## 정리

- **클로드 코드는 유료 요금제(Pro·Max·Team·Enterprise)나 Claude Console 계정으로 쓸 수 있습니다.** 무료 요금제로는 쓸 수 없습니다.
- **설치는 네이티브 설치 프로그램 한 줄이 추천**입니다. 윈도우 PowerShell이라면 `irm https://claude.ai/install.ps1 | iex`입니다.
- **npm판에서 `running scripts is disabled`가 뜨면** `claude.cmd`로 실행하거나, 실행 정책을 `RemoteSigned`(CurrentUser)로 바꾸거나, 네이티브로 다시 설치합니다.
- **작업할 폴더에서 `claude`를 실행하고 한국어로 그대로 부탁하면 됩니다.** 이번 연습에서는 파일 하나 만드는 데 약 3초가 걸렸습니다.
- **기본값은 auto mode**입니다. 불안하면 Shift+Tab으로 확인 창이 뜨는 모드로 바꾸고, 사용량은 `/usage`로 확인합니다.

## 자주 묻는 질문

**클로드 코드는 무료로 쓸 수 있나요?**
쓸 수 없습니다. 공식 문서에 클로드 무료 요금제에는 클로드 코드가 포함되지 않는다고 나와 있습니다. Pro 이상 요금제나 Claude Console(API 종량제) 계정이 필요합니다.

**클로드 코드는 한국어로 쓸 수 있나요?**
네. 지시는 한국어로 그대로 쓰면 됩니다. 메뉴와 화면 표시는 영어지만, 이번 테스트에서도 한국어로 지시하자 한국어로 답이 왔습니다.

**윈도우에서 WSL이 꼭 필요한가요?**
필요 없습니다. PowerShell이나 CMD에서 바로 설치해서 쓸 수 있습니다. 리눅스 도구를 쓰거나 샌드박스 기능이 필요할 때는 WSL 2를 고릅니다.

**`claude`를 치면 "running scripts is disabled"가 떠요.**
npm으로 설치했을 때 나는 PowerShell 실행 정책 오류입니다. `claude.cmd`로 실행하거나, `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`를 실행하거나, 네이티브 설치 프로그램으로 다시 설치하세요.

**클로드 코드와 데스크톱 앱 사용량은 따로인가요?**
같습니다. 구독 요금제에서는 클로드 코드와 클로드 앱(웹·데스크톱·모바일)이 같은 한도를 함께 씁니다.

**VS Code 안에서도 쓸 수 있나요?**
쓸 수 있습니다. 공식 VS Code·JetBrains 확장 프로그램이 있어서 에디터 안에서 클로드 코드를 쓸 수 있습니다.

## 비용 계산해 보기

클로드 코드를 구독으로 쓸지 API 종량제로 쓸지 고민된다면 [코딩 에이전트 비용 계산기](/ko/agents)로 한 달 API 비용을 계산해서 Pro·Max와 비교해 보세요. 구독과 API 중 어느 쪽이 싼지는 [구독 vs API 계산기](/ko/plans)로도 확인할 수 있습니다.

*설치 방법과 실행 조건은 2026년 10월 12일 클로드 코드 공식 문서에서 확인했습니다. 화면은 윈도우 PowerShell, Claude Code v2.1.295 기준입니다.*

## 출처

- [Claude Code Docs: Advanced setup](https://code.claude.com/docs/en/setup)
- [Claude Code Docs: Quickstart](https://code.claude.com/docs/en/quickstart)
- [Claude Code Docs: Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)
- [Claude Code Docs: Commands](https://code.claude.com/docs/en/commands)
- [Claude Code Docs: Choose a permission mode](https://code.claude.com/docs/en/permission-modes)
- [Anthropic: Claude plans and pricing](https://claude.com/pricing)
- [Microsoft Learn: about_Execution_Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)
<!-- autoimg -->
