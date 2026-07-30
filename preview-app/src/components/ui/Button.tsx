import React from 'react';

type ButtonVariant = 'solid' | 'outline' | 'icon';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  children: React.ReactNode;
  icon?: React.ReactNode;
}

export function Button({ variant = 'solid', children, icon, className = '', ...props }: ButtonProps) {
  let baseClasses = "flex items-center justify-center font-bold text-sm leading-5 rounded-full transition-colors ";
  
  if (variant === 'solid') {
    baseClasses += "bg-brand-solid text-white px-4 py-2.5 gap-1 hover:bg-blue-600 ";
  } else if (variant === 'outline') {
    baseClasses += "bg-white text-text-brand border border-border-brand px-4 py-2.5 gap-1 hover:bg-brand-secondary ";
  } else if (variant === 'icon') {
    baseClasses += "bg-white border border-border-brand p-3 hover:bg-brand-secondary ";
  }

  return (
    <button className={`${baseClasses} ${className}`} {...props}>
      {icon && <span className="flex-shrink-0">{icon}</span>}
      {children}
    </button>
  );
}
