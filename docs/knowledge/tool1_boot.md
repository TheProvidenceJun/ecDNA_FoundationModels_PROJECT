# 도구1 (챗봇) 새 채팅 부팅 규칙

> 이건 사람(JUN)의 운영 메모다. cowork·codex는 안 읽는다.
> 챗봇(도구1)은 로컬 docs를 못 읽어서 새 채팅마다 빈손으로 시작한다.
> 그래서 새 채팅을 열 때 아래를 직접 첨부해 부팅시킨다.
> ※ 아래는 '어떤 파일을 붙일지' 가리키는 포인터다. 내용 사본이 아니므로
>   원본이 바뀌어도 이 규칙은 안 틀린다.

## 매 새 채팅에 항상 첨부 (3개)
- docs/state/STATE.md        — 지금 어디 (가장 중요. 하나만 붙여야 하면 이것)
- docs/plan/current_phase.md — 이 단계 목표·완료조건
- CLAUDE.md                  — 협업 구조·쓰기경계 (거의 안 바뀜)

## 그날 작업에 따라 추가
- 그 라운드에서 검증·논의할 cowork 산출물 (초안 spec, 갱신된 문서 등)
- (phase 전환·큰그림 논의 시) docs/plan/roadmap.md
- ("전에 왜 이렇게 정했지?"가 쟁점일 때) docs/log/decisions.md 최근 항목

## Phase A부터 추가
- docs/knowledge/ 의 관련 학습 노트
- docs/knowledge/ecDNA_FM_guide.md  (도메인 배경)

## 안 붙여도 되는 것
- AGENTS.md / constraints.md / roles.md / conventions.md
  → 그 문서 자체를 손보는 날이 아니면 불필요 (평소엔 CLAUDE.md 요약으로 충분)
- sessions.md 전체 → 직전 상황은 STATE가 담음. 옛 히스토리가 쟁점일 때만.

## 첨부와 함께
- 첫 메시지에 "오늘 ___ 하려 한다" 한 줄 같이 적기.
  → 파일이 '어디 있나'를 주고, 이 한 줄이 '오늘 뭐 할까'를 줘서 부팅이 또렷해진다.

## 주의 (rot 방지)
- STATE가 최신인지 사람이 책임진다. cowork가 세션 끝에 STATE 갱신을 빼먹으면
  도구1이 옛 상태로 부팅하니, 새 채팅 열기 전 STATE의 last-updated를 확인.
