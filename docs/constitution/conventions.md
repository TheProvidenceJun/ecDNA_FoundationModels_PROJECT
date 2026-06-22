<!--
last-updated: 2026-06-21
session-id: 2026-06-21-constitution-roles-conventions
author-agent: cowork
-->

# conventions.md — 파일 / 네이밍 / 헤더 / 커밋 규약

> 지금까지 암묵적으로 써온 규칙을 명문화한다. **codex가 smoke test에서 실제로 따를
> 규약**이라, 모호하면 codex가 막힌다. 따라서 가능한 한 구체적으로 적는다.
> ⚠️ 표시는 **이번 세션에 새로 정한(또는 기본값을 제안한) 항목** — 사람 합의 대상.

---

## 1. 문서 헤더

**덮어쓰기형 문서**(constitution / plan / state / tasks/specs / tasks/reports)는 머리에
HTML 주석 헤더를 단다:

```
<!--
last-updated: YYYY-MM-DD
session-id: <session-id>
author-agent: cowork | codex
-->
```

**append-only 로그**(`log/sessions.md`, `log/decisions.md`)는 위 헤더 대신 각 항목에
날짜·작성자를 포함하는 줄 단위 형식을 쓴다(§4·§5 참조).

`docs/knowledge/`는 사람(도구1) 소유라 헤더를 강제하지 않는다.

### session-id 형식
`YYYY-MM-DD-<짧은꼬리표>` (예: `2026-06-21-plan-fill`).
- 꼬리표는 그 세션이 한 일을 짧게 나타낸다(영문 소문자-하이픈).
- **같은 날 여러 세션이면 꼬리표로 구분**한다(예: `2026-06-21-agents-md`, `2026-06-21-plan-fill`).

---

## 2. 파일명 규칙 — spec / report

| 종류 | 형식 | 예 |
|---|---|---|
| spec | `tasks/specs/SPEC-<번호>-<짧은제목>.md` | `SPEC-001-smoke-test.md` |
| report | `tasks/reports/REPORT-<같은번호>-<짧은제목>.md` | `REPORT-001-smoke-test.md` |

- **번호는 3자리 0 패딩, 001부터 시작, 1씩 증가.** ⚠️(새로 확정 — 템플릿 예시 `SPEC-001`과 일치시킴.)
- **report 번호 = 짝 spec 번호**(같은 작업의 계약 쌍이므로). 짧은제목도 가급적 일치.
- 짧은제목: 영문 소문자-하이픈, 2~4단어.
- `_TEMPLATE.md`는 번호 없이 그대로 두며 복제용 원본이다(작업 파일 아님).

---

## 3. 산출물 위치 (codex 코드·결과물) — (2026-06-21 확정)

템플릿이 이미 `outputs/`·`scripts/`를 암시하고 있어 그에 맞춰 확정한다:

| 종류 | 위치 | 비고 |
|---|---|---|
| 실행 스크립트·코드 | `scripts/` | 재현 가능한 코드 |
| 생성 결과물(그림·표·embedding 등) | `outputs/` | report가 가리키는 산출물 |
| 데이터 | `data/` | **git에 추적하지 않는다(.gitignore 대상).** 대용량 정책(LFS 등)은 Phase A 데이터 반입 전에 별도로 정한다. |

- spec은 §4(산출물)에서 **정확한 파일 경로**를 지정하고, report는 그 경로를 추적 흔적으로 되짚는다.
- 위 폴더는 아직 저장소에 없을 수 있다. 첫 codex 작업(또는 smoke test) 때 생성.

---

## 4. 커밋 메시지 규약 (커밋 자체는 사람이 한다) — (2026-06-21 확정)

> **git commit/push는 사람 전용**(CLAUDE.md §4). cowork는 메시지를 *제안*만 한다.

**표준 형식**: `<type>: <요약>` — **type 바로 뒤에 콜론, 콜론 뒤에만 공백 한 칸.**
```
docs: scaffold docs/
docs: add AGENTS.md (codex boot entrypoint); update STATE/plan/decisions
docs: add ecDNA_FM_guide to knowledge/
```
- type: `docs` / `spec` / `report` / (코드 시) `feat`·`fix` 등.
- 여러 변경은 `;`로 구분하거나 본문 줄바꿈.
- 언어: 한·영 혼용 허용(요약은 읽기 쉬운 쪽으로). 소문자 시작.

> [^1] **히스토리 정직성**: 위 예시는 표준형으로 *다시 적은* 것이다. 실제 과거 커밋
> (`d55b6d1`, `a9817a4`, `4bb28f7`)은 구형식 `docs : ` (콜론 양옆 공백)로 기록돼 있다.
> 과거 메시지는 위조·rewrite 하지 않는다. **앞으로의 커밋만 표준형으로 통일**한다.
> (통일 결정: `log/decisions.md` 2026-06-21.)

---

## 5. 로그 기록 형식

- **`log/sessions.md`** (append-only): `날짜 / session-id / author / 무엇을 했나` 한 줄.
- **`log/decisions.md`** (append-only, cowork만): 항목당 `## YYYY-MM-DD — 제목` + `무엇을 / 왜 / 대안은`.

---

## 6. 표기 일관성

- **날짜**: `YYYY-MM-DD` (예: 2026-06-21). 다른 형식 쓰지 않는다.
- **번호**: spec/report는 3자리 0 패딩(§2). Phase는 문자(A~E)와 소수 단계(A.3 등) 표기.
- **체크박스**: 완료 판정에만 사용하고, 한 항목은 한 곳에서만 판정한다(중복 판정 금지 — rot 방지).
- **포인터 우선**: 원문이 있는 규칙은 복붙하지 말고 "상세는 X 참조"로 가리킨다.
