-- ============================================================
--  Cloud sync for the portfolio — run this ONCE.
--
--  Supabase dashboard  ->  SQL Editor  ->  New query
--  Paste EVERYTHING below, press RUN.
--
--  What it does:
--    * stores your links + profile picture in one row
--    * ANYONE may read it      (so every visitor sees your links)
--    * NOBODY may write it     without the admin password
--
--  The anon key in your HTML is public by design. It cannot write,
--  because the password is verified inside the database by a
--  function the anon key is not allowed to read.
-- ============================================================

-- ---------- 1. the settings table ----------------------------
create table if not exists public.site_config (
  id         int primary key,
  data       jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

insert into public.site_config (id, data)
values (1, '{}'::jsonb)
on conflict (id) do nothing;

-- reads are public, writes go through the function below only
alter table public.site_config enable row level security;

drop policy if exists "public read"  on public.site_config;
drop policy if exists "admin update" on public.site_config;
drop policy if exists "no direct write" on public.site_config;

create policy "public read"
  on public.site_config
  for select
  using (true);

-- deliberately NO insert/update/delete policy:
-- direct writes with the anon key are impossible.

grant select on public.site_config to anon, authenticated;

-- ---------- 2. the password (never readable publicly) --------
create table if not exists public.private_admin (
  id   int primary key,
  pass text not null
);

alter table public.private_admin enable row level security;
-- no policy + no grant => the anon key can never touch this table.
revoke all on public.private_admin from anon, authenticated;

-- >>>>>>>>>>  CHANGE THIS PASSWORD  <<<<<<<<<<
insert into public.private_admin (id, pass)
values (1, 'onyx2026')
on conflict (id) do update set pass = excluded.pass;

-- ---------- 3. the only way to write -------------------------
--  SECURITY DEFINER runs as the owner, so it can read the
--  password table and bypass RLS — but only after checking
--  the password the caller supplied.
create or replace function public.save_site_config(p_pass text, p_data jsonb)
returns boolean
language plpgsql
security definer
set search_path = public
as $$
declare
  ok boolean;
begin
  select exists (
    select 1 from public.private_admin
    where id = 1 and pass = p_pass
  ) into ok;

  if not ok then
    raise exception 'invalid admin password' using errcode = '42501';
  end if;

  update public.site_config
     set data = p_data,
         updated_at = now()
   where id = 1;

  return true;
end;
$$;

revoke all on function public.save_site_config(text, jsonb) from public;
grant execute on function public.save_site_config(text, jsonb) to anon, authenticated;

-- ---------- 4. optional: change the password later -----------
create or replace function public.change_admin_password(p_old text, p_new text)
returns boolean
language plpgsql
security definer
set search_path = public
as $$
declare
  ok boolean;
begin
  select exists (
    select 1 from public.private_admin where id = 1 and pass = p_old
  ) into ok;

  if not ok then
    raise exception 'invalid admin password' using errcode = '42501';
  end if;

  update public.private_admin set pass = p_new where id = 1;
  return true;
end;
$$;

revoke all on function public.change_admin_password(text, text) from public;
grant execute on function public.change_admin_password(text, text) to anon, authenticated;

-- ============================================================
--  DONE.
--
--  Next: Settings -> API, copy
--     Project URL      https://aektkaxoobrovvermymv.supabase.co
--     anon public key  (the long key labelled "anon" / "public")
--
--  Then: your site -> admin panel -> Cloud sync ->
--        paste both + the password above -> "Connect & sync".
-- ============================================================
