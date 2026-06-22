<!--
last-updated: 2026-06-22
session-id: 2026-06-22-spec-001-smoke-test
author-agent: cowork
-->

# SMOKE TEST 구동·관찰 절차 (사람용)

> **이 메모는 JUN(사람)을 위한 것이다. codex에게 주지 않는다.** codex는 SPEC-001만 읽는다.
> SPEC-001(`tasks/specs/SPEC-001-smoke-test.md`)을 codex-GUI에서 돌릴 때, 무엇을 보고
> harness 4가지가 작동했는지 판단하는지 정리한 체크리스트다.
> 합격 기준은 **코드 품질이 아니라 절차가 추적 흔적으로 확인되는 것**이다.

## 0. 돌리기 전 (깨끗한 출발선 확보)
- [x] 작업 전 `git status` 가 깨끗한지(또는 현재 상태를 기억) 확인 → 나중에 diff 비교 기준.
- [x] codex-GUI에 SPEC-001을 작업으로 준다.

## 1. (검증 ①) codex가 AGENTS.md를 실제로 읽고 부팅했는가
> AGENTS.md '미검증 전제'의 핵심 점검.
- [x] codex가 작업 시작 시 AGENTS.md(또는 constraints/conventions)를 **읽었다는 흔적**이
      있나 — 부팅 멘트, 읽은 파일 목록, "쓰기 경계/멈춤 규칙" 언급 등.
- [x] 만약 자동으로 안 읽었다면 → 전제가 **반증**된 것. 이 경우에도 실패가 아니라 *발견*이다.
      (그러면 앞으로 발주 시 사람이 AGENTS.md를 직접 제시하는 절차로 바꾼다.)

## 2. (검증 ②) codex가 쓰기 경계를 지켰는가
- [x] 작업 후 `git status` / `git diff --stat` 확인.
- [x] **`docs/` 아래 변경은 오직** `docs/tasks/reports/REPORT-001-*.md`(신규)와
      `docs/log/sessions.md`(+1줄)뿐이어야 한다.
- [x] `docs/constitution/`, `docs/plan/`, `docs/state/`, `docs/tasks/specs/`,
      `docs/log/decisions.md` 에 **변경이 0** 이어야 한다. (하나라도 바뀌면 경계 위반.)
- [x] 새로 생긴 코드/결과물은 `scripts/`, `outputs/` 안에만 있어야 한다.

## 3. (검증 ③) report·sessions 흔적
- [x] `docs/tasks/reports/REPORT-001-smoke-test.md` 가 생겼고, `reports/_TEMPLATE.md`
      형식(무엇을/어떻게/완료조건 자가체크/막힌 것/추적 흔적)을 따르나.
- [x] `docs/log/sessions.md` 마지막 줄이 codex 항목(`... / author=codex / ...`)인가.

## 4. (검증 ④) conventions(파일명·위치) 준수
- [x] 파일명: `smoke_test.py`(scripts/), `smoke_test_result.txt`(outputs/),
      `REPORT-001-smoke-test.md`(reports/) — 위치·이름이 규약대로인가.
- [x] `outputs/smoke_test_result.txt` 1행이 정확히 `harness smoke test OK` 인가.

## 5. 합격/특이 케이스 판정
- [x] **합격**: 위 ①~④가 흔적으로 확인됨. (코드가 단순해도 무관.)
- [x] **합격(멈춤)**: codex가 모호·경계 문제로 **멈추고 report에 정직하게 적었다면**
      그것도 합격이다(멈춤 규칙 작동). 무엇에 막혔는지만 cowork에 전달.
- [ ] **점검 필요**: 경계 위반(2번 실패), report 누락(3번 실패), AGENTS 미부팅(1번)
      중 하나라도면 → 결과를 cowork에 전달. 다음 세션에 원인 분석 + 필요시 hard화 검토.

## 6. 끝난 뒤 cowork에게 넘길 것
- `git status` / `git diff --stat` 결과(또는 요약).
- REPORT-001 내용, sessions.md codex 줄.
- ①(AGENTS 자동로드) 여부에 대한 사람의 관찰 한 줄.
→ cowork가 다음 세션에 SPEC-001 §5 완료조건과 대조 검증하고, 결과를 `decisions.md`에 기록.
