import React from 'react';

interface InfoCellProps {
  label: string;
  value: React.ReactNode;
  rightIcon?: React.ReactNode;
  onClick?: () => void;
  className?: string;
}

export function InfoCell({ label, value, rightIcon, onClick, className = '' }: InfoCellProps) {
  return (
    <div 
      className={`flex items-center justify-between py-2 w-full ${onClick ? 'cursor-pointer hover:bg-gray-50' : ''} ${className}`}
      onClick={onClick}
    >
      <p className="text-sm font-normal text-text-secondary">{label}</p>
      <div className="flex items-center gap-1 justify-end">
        {typeof value === 'string' ? (
          <p className="text-sm font-bold text-text-primary text-right">{value}</p>
        ) : (
          value
        )}
        {rightIcon && <span className="flex-shrink-0">{rightIcon}</span>}
      </div>
    </div>
  );
}
