-- ============================================================
--  COMPATIBILITY PATCH
--  Run this if the site currently online is the older build that
--  writes with PATCH {data, pass} instead of the save_site_config
--  RPC. It lets BOTH the old and the new build save correctly.
--
--  Supabase -> SQL Editor -> New query -> paste -> RUN
-- ============================================================

-- the old client sends a "pass" field, so the column must exist
alter table public.site_config
  add column if not exists pass text;

-- checks the password without exposing private_admin
create or replace function public.check_admin(p text)
returns boolean
language sql
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.private_admin where id = 1 and pass = p
  );
$$;

revoke all on function public.check_admin(text) from public;
grant execute on function public.check_admin(text) to anon, authenticated;

-- wipe the password AFTER the policy has checked it, so it is
-- never stored in the publicly readable row.
create or replace function public.clear_pass()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  if new.pass is not null then
    update public.site_config set pass = null where id = new.id;
  end if;
  return null;
end;
$$;

drop trigger if exists site_config_strip_pass on public.site_config;
drop trigger if exists site_config_clear_pass on public.site_config;

create trigger site_config_clear_pass
  after insert or update on public.site_config
  for each row execute function public.clear_pass();

-- allow direct updates, but only when the password is correct
drop policy if exists "admin update" on public.site_config;

create policy "admin update"
  on public.site_config
  for update
  using (true)
  with check (public.check_admin(pass));

grant update on public.site_config to anon, authenticated;

-- ============================================================
--  DONE. The old site can now save, and the new build keeps
--  working through save_site_config().
-- ============================================================
