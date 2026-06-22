<!--
last-updated: 2026-06-22
session-id: 2026-06-22-spec-001-smoke-test
author-agent: cowork
-->

# SPEC-001 — harness smoke test (더미 스크립트 + 경계 준수)

> 너(codex)는 AGENTS.md + 이 spec만 읽고 일한다. 이 프로젝트의 다른 맥락은 몰라도 된다.
> 이 작업은 **자기완결적**이다 — 아래에 적힌 것만으로 처음부터 끝까지 수행 가능하다.

| 항목 | 값 |
|---|---|
| spec-id | SPEC-001 |
| 발주일 | 2026-06-22 |
| 발주자 | cowork |
| 연결 단계 | 협업 harness 검증 (smoke test) |
| 우선순위 | 상 |
| 짝 report | REPORT-001 (네가 작성) |

## 1. 무엇을 (What)
간단한 Python 스크립트 1개(`scripts/smoke_test.py`)를 만들고, 그것을 실행해 결과를
`outputs/smoke_test_result.txt`로 남긴다. 그게 전부다.

## 2. 왜 (Why)
이 작업의 목적은 **코드 실력 평가가 아니라 협업 절차(spec→구현→report)가 실제로
작동하는지 처음으로 시험**하는 것이다. 따라서 작업 자체는 의도적으로 사소하다.
중요한 것은 네가 (a) 부팅 규약대로 읽고, (b) 쓰기 경계를 지키고, (c) report를
형식대로 남기고, (d) 파일명·위치 규약을 지키는지다. **막히면 추측하지 말고 멈추고
report에 적는 것도 정상 동작이다.**

## 3. 입력 (Inputs)
없음. (외부 데이터·이전 산출물 불필요.)

## 4. 산출물 (Outputs)
정확히 다음 두 파일을 생성한다(폴더가 없으면 폴더부터 생성):

1. **`scripts/smoke_test.py`** — 실행 시 아래 4줄을 **표준출력으로 print** 하고,
   동시에 같은 4줄을 `outputs/smoke_test_result.txt`에 **쓴다(overwrite)**:
   - 1행: 고정 문자열 `harness smoke test OK`
   - 2행: `python: ` + 현재 파이썬 버전 (`sys.version.split()[0]`)
   - 3행: `utc: ` + 현재 UTC 시각 ISO8601 (예: `2026-06-22T07:30:00Z`)
   - 4행: `platform: ` + OS/플랫폼 문자열 (`platform.platform()`)
   - 표준 라이브러리만 사용한다(`sys`, `platform`, `datetime`). 외부 패키지 설치 금지.

2. **`outputs/smoke_test_result.txt`** — 위 스크립트를 1회 실행한 결과(위 4줄).

> 파일명·위치 규약은 `docs/constitution/conventions.md` §3(산출물 위치)을 따른다:
> 코드는 `scripts/`, 결과물은 `outputs/`.

## 5. 완료조건 (Done = 검증 가능하게) ⚠️ 가장 중요
네가 report에서 자가체크하고, cowork가 다음 세션에 yes/no로 대조할 항목:

- [ ] `scripts/smoke_test.py` 가 생성됨 (표준 라이브러리만 사용).
- [ ] `outputs/smoke_test_result.txt` 가 존재하고, 1행이 정확히 `harness smoke test OK`.
- [ ] 결과 파일에 `python:` / `utc:` / `platform:` 3줄이 모두 있음.
- [ ] `docs/` 아래에서 **`docs/tasks/reports/` 신규 파일과 `docs/log/sessions.md` 한 줄 append를
      제외하고는 아무것도 변경되지 않음** (constitution/plan/state/specs/decisions 무수정).
- [ ] `REPORT-001-smoke-test.md` 가 `docs/tasks/reports/_TEMPLATE.md` 형식대로
      `docs/tasks/reports/` 에 작성됨 (완료조건 자가체크 + 추적 흔적 포함).
- [ ] `docs/log/sessions.md` 에 codex 항목 한 줄 append됨
      (형식: `날짜 / session-id / author=codex / 무엇을 했나`).
- [ ] 재현 명령(예: `python scripts/smoke_test.py`)이 report의 추적 흔적에 적힘.

## 6. 건드리지 말 것 (Out of scope / Do-not-touch)
- **`docs/` 전체는 수정 금지.** 예외는 단 둘: `docs/tasks/reports/`에 네 report 신규 작성,
  `docs/log/sessions.md`에 한 줄 append. 그 외 `docs/constitution/`, `docs/plan/`,
  `docs/state/`, `docs/tasks/specs/`, `docs/log/decisions.md`는 **읽기만** 하고 절대 고치지 마라.
- 이 spec 파일(`SPEC-001-smoke-test.md`)을 수정하지 마라.
- `scripts/`, `outputs/` 외의 코드/폴더를 새로 만들거나 고치지 마라.
- **git commit / push 하지 마라** (사람 전용). 파일을 디스크에 쓰는 데까지가 네 일이다.
- 작업 범위를 "도움이 되려고" 넓히지 마라. 위 4·5번에 적힌 것만 한다.

## 7. 위험·승인 필요
없음. (영구 삭제·권한 변경·외부 공유 등 위험 요소 없음.)
