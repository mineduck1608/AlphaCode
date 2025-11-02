/**
 * WebSocket Connection Status Badge
 */

'use client';

import { Circle } from 'lucide-react';
import { cn } from '@/app/lib/utils';

interface ConnectionStatusProps {
  connected: boolean;
  connecting?: boolean;
  className?: string;
}

export function ConnectionStatus({ connected, connecting, className }: ConnectionStatusProps) {
  return (
    <div className={cn('flex items-center gap-2 text-sm', className)}>
      <Circle
        className={cn(
          'w-2 h-2',
          connected && 'fill-green-500 text-green-500',
          connecting && 'fill-yellow-500 text-yellow-500 animate-pulse',
          !connected && !connecting && 'fill-red-500 text-red-500'
        )}
      />
      <span className="text-xs">
        {connecting && 'Đang kết nối...'}
        {connected && !connecting && 'Đã kết nối'}
        {!connected && !connecting && 'Chưa kết nối'}
      </span>
    </div>
  );
}
