# Creates a manifest that kill a process

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
