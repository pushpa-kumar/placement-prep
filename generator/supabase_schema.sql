create table progress (
  user_id uuid references auth.users(id) on delete cascade not null,
  item_id text not null,
  item_type text not null,
  done_at timestamptz not null default now(),
  primary key (user_id, item_id)
);

alter table progress enable row level security;

create policy "read own progress"
  on progress for select
  using (auth.uid() = user_id);

create policy "insert own progress"
  on progress for insert
  with check (auth.uid() = user_id);

create policy "delete own progress"
  on progress for delete
  using (auth.uid() = user_id);
